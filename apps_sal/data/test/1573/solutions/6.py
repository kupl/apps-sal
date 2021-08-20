import unittest
import sys


class Company:
    """ Company representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """
        it = iter(test_inputs.split('\n')) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()
        [self.n, self.d] = list(map(int, uinput().split()))
        pairs = ' '.join((uinput() for i in range(self.n))).split()
        self.numa = [int(pairs[i]) for i in range(0, 2 * self.n, 2)]
        self.numb = [int(pairs[i]) for i in range(1, 2 * self.n, 2)]
        self.money = [(self.numa[i], self.numb[i]) for i in range(self.n)]
        self.money = sorted(self.money)
        self.partsum = [0]
        sum = 0
        for i in range(self.n):
            sum += self.money[i][1]
            self.partsum.append(sum)

    def calculate(self):
        """ Main calcualtion function of the class """
        result = 0
        for i in range(self.n):
            mlb = self.money[i][0]
            mrb = mlb + self.d
            ilb = i
            irb = lbound(self.money, mrb)
            sumf = self.partsum[irb] - self.partsum[ilb]
            result = max(result, sumf)
        return str(result)


def lbound(v, n):
    b = 0
    e = len(v)
    while b != e:
        mid = (b + e) // 2
        if v[mid][0] < n:
            b = mid + 1
        else:
            e = mid
    return b


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Company class testing """
        test = '4 5\n75 5\n0 100\n150 20\n75 1'
        d = Company(test)
        self.assertEqual(d.n, 4)
        self.assertEqual(d.d, 5)
        self.assertEqual(d.numa, [75, 0, 150, 75])
        self.assertEqual(d.numb, [5, 100, 20, 1])
        self.assertEqual(Company(test).calculate(), '100')
        test = '5 100\n0 7\n11 32\n99 10\n46 8\n87 54'
        self.assertEqual(Company(test).calculate(), '111')
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
        d = Company(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print('\nTimelimit Test: ' + '{0:.3f}s (init {1:.3f}s calc {2:.3f}s)'.format(stop - start, calc - start, stop - calc))


def __starting_point():
    sys.setrecursionlimit(100000)
    if sys.argv[-1] == '-ut':
        unittest.main(argv=[' '])
    sys.stdout.write(Company().calculate())


__starting_point()
