import unittest
import sys


class Beach:
    """ Beach representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """
        it = iter(test_inputs.split('\n')) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()
        [self.n] = list(map(int, uinput().split()))
        self.nums = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """
        (result, u) = (0, 0)
        tp = sorted([(n, i) for (i, n) in enumerate(self.nums)])
        for i in range(self.n):
            u = max(u, tp[i][1])
            if i >= u:
                result += 1
        return str(result)


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Beach class testing """
        test = '3\n1 2 3'
        d = Beach(test)
        self.assertEqual(d.n, 3)
        self.assertEqual(d.nums, [1, 2, 3])
        self.assertEqual(Beach(test).calculate(), '3')
        test = '4\n2 1 3 2'
        self.assertEqual(Beach(test).calculate(), '2')
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
        d = Beach(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print('\nTimelimit Test: ' + '{0:.3f}s (init {1:.3f}s calc {2:.3f}s)'.format(stop - start, calc - start, stop - calc))


def __starting_point():
    sys.setrecursionlimit(100000)
    if sys.argv[-1] == '-ut':
        unittest.main(argv=[' '])
    sys.stdout.write(Beach().calculate())


__starting_point()
