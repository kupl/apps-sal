
import unittest
import sys


class Cowbell:
    """ Cowbell representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        [self.n, self.k] = list(map(int, uinput().split()))

        self.nums = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """

        b = self.nums[self.n - self.k:]
        for i in range(self.n - self.k):
            b[i] += self.nums[self.n - self.k - 1 - i]
        result = max(b)

        return str(result)


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Cowbell class testing """

        test = "2 1\n2 5"
        d = Cowbell(test)
        self.assertEqual(d.n, 2)
        self.assertEqual(d.k, 1)
        self.assertEqual(d.nums, [2, 5])

        self.assertEqual(Cowbell(test).calculate(), "7")

        test = "4 3\n2 3 5 9"
        self.assertEqual(Cowbell(test).calculate(), "9")

        test = "3 2\n3 5 7"
        self.assertEqual(Cowbell(test).calculate(), "8")

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
        d = Cowbell(test)
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

    sys.stdout.write(Cowbell().calculate())


__starting_point()
