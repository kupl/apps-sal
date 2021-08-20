import unittest
import sys


class Bear:
    """ Bear representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """
        it = iter(test_inputs.split('\n')) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()
        self.n = int(uinput())
        self.nums = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """
        lamak = self.nums[0]
        srt = sorted(self.nums[1:])
        result = 0
        while lamak <= srt[-1]:
            srt[-1] -= 1
            lamak += 1
            result += 1
            srt = sorted(srt)
        return str(result)


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Bear class testing """
        test = '5\n5 1 11 2 8'
        d = Bear(test)
        self.assertEqual(d.n, 5)
        self.assertEqual(d.nums, [5, 1, 11, 2, 8])
        self.assertEqual(Bear(test).calculate(), '4')
        test = '4\n1 8 8 8'
        self.assertEqual(Bear(test).calculate(), '6')
        test = '2\n7 6'
        self.assertEqual(Bear(test).calculate(), '0')
        test = '4\n0 1 1 1'
        self.assertEqual(Bear(test).calculate(), '2')
        self.time_limit_test(100)

    def time_limit_test(self, nmax):
        """ Timelimit testing """
        import random
        import timeit
        test = str(nmax) + '\n'
        test += '0 '
        nums = [1000 for i in range(nmax - 1)]
        test += ' '.join(map(str, nums)) + '\n'
        start = timeit.default_timer()
        d = Bear(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print('\nTimelimit Test: ' + '{0:.3f}s (init {1:.3f}s calc {2:.3f}s)'.format(stop - start, calc - start, stop - calc))


def __starting_point():
    sys.setrecursionlimit(100000)
    if sys.argv[-1] == '-ut':
        unittest.main(argv=[' '])
    sys.stdout.write(Bear().calculate())


__starting_point()
