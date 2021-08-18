
import unittest
import sys


class Steps:
    """ Steps representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        [self.n] = list(map(int, uinput().split()))

        self.nums = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """

        maxsf = 0
        maxc = 0

        for i in range(len(self.nums)):
            if i != 0:
                if self.nums[i] >= self.nums[i - 1]:
                    maxc += 1
                    maxsf = max(maxsf, maxc)
                else:
                    maxc = 0

        return str(maxsf + 1)


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Steps class testing """

        test = "6\n2 2 1 3 4 1"
        d = Steps(test)
        self.assertEqual(d.n, 6)
        self.assertEqual(d.nums[0:3], [2, 2, 1])

        self.assertEqual(Steps(test).calculate(), "3")

        test = "3\n2 2 9"
        self.assertEqual(Steps(test).calculate(), "3")

        test = "2\n0"
        self.assertEqual(Steps(test).calculate(), "1")
        test = "2\n0 0"
        self.assertEqual(Steps(test).calculate(), "2")
        test = "3\n0 -1 1 1"
        self.assertEqual(Steps(test).calculate(), "3")

        test = ""

    def time_limit_test(self, nmax):
        """ Timelimit testing """
        import random
        import timeit

        test = str(nmax) + " " + str(nmax) + "\n"
        numnums = [str(i) + " " + str(i + 1) for i in range(nmax)]
        test += "\n".join(numnums) + "\n"
        nums = [random.randint(1, 10000) for i in range(nmax)]
        test += " ".join(map(str, nums)) + "\n"

        start = timeit.default_timer()
        d = Steps(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print(("\nTimelimit Test: " +
              "{0:.3f}s (init {1:.3f}s calc {2:.3f}s)".
               format(stop - start, calc - start, stop - calc)))


def __starting_point():

    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    sys.stdout.write(Steps().calculate())


__starting_point()
