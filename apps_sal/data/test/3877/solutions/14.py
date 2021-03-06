import unittest
import sys


class Code:
    """ Code representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """
        it = iter(test_inputs.split('\n')) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()
        [self.n, self.l, self.r] = list(map(int, uinput().split()))

    def bitlist(self, n):
        result = []
        while n > 0:
            result.append(n & 1)
            n = int(n / 2)
        result.reverse()
        return result

    def period(self, i):
        return 2 << i

    def start(self, i):
        return (1 << i) - 1

    def count(self, s, p, l, r):
        start = 1 if (l - s) % p == 0 else 0
        return (r - s) // p - (l - s) // p + start

    def calculate(self):
        """ Main calcualtion function of the class """
        result = 0
        bl = self.bitlist(self.n)
        for (i, n) in enumerate(bl):
            if n == 1:
                period = self.period(i)
                start = self.start(i)
                result += self.count(start, period, self.l - 1, self.r - 1)
        return str(result)


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Code class testing """
        test = '7 2 5'
        d = Code(test)
        self.assertEqual(d.n, 7)
        self.assertEqual(d.l, 2)
        self.assertEqual(d.r, 5)
        self.assertEqual(Code(test).calculate(), '4')
        self.assertEqual(d.bitlist(6), [1, 1, 0])
        self.assertEqual(d.bitlist(6)[0], 1)
        self.assertEqual(d.period(0), 2)
        self.assertEqual(d.period(2), 8)
        self.assertEqual(d.start(0), 0)
        self.assertEqual(d.start(3), 7)
        self.assertEqual(d.count(6, 8, 3, 5), 0)
        self.assertEqual(d.count(6, 8, 5, 14), 2)
        test = '10 3 10'
        self.assertEqual(Code(test).calculate(), '5')
        test = '20000000 0 0'
        self.assertEqual(Code(test).calculate(), '0')
        test = ''
        test = ''

    def time_limit_test(self, nmax):
        """ Timelimit testing """
        import random
        import timeit
        test = str(nmax) + ' ' + str(nmax) + '\n'
        numnums = [str(i) + ' ' + str(i + 1) for i in range(nmax)]
        test += '\n'.join(numnums) + '\n'
        nums = [random.randint(1, 10000) for i in range(nmax)]
        test += ' '.join(map(str, nums)) + '\n'
        start = timeit.default_timer()
        d = Code(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print('\nTimelimit Test: ' + '{0:.3f}s (init {1:.3f}s calc {2:.3f}s)'.format(stop - start, calc - start, stop - calc))


def __starting_point():
    sys.setrecursionlimit(100000)
    if sys.argv[-1] == '-ut':
        unittest.main(argv=[' '])
    sys.stdout.write(Code().calculate())


__starting_point()
