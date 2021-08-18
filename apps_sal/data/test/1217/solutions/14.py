
import unittest
import sys


def rbound(v, n):
    b = 0
    e = len(v)
    while b != e:
        mid = (b + e + 1) // 2
        if v[mid - 1] <= n:
            b = mid
        else:
            e = mid - 1
    return b


class Query:
    """ Query representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        [self.n, self.m] = list(map(int, uinput().split()))

        self.numa = list(map(int, uinput().split()))
        self.numb = list(map(int, uinput().split()))

        self.snuma = sorted(self.numa)

    def calculate(self):
        """ Main calcualtion function of the class """

        result = []
        for n in self.numb:
            result.append(rbound(self.snuma, n))

        return str(" ".join(map(str, result)))


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Query class testing """

        test = "5 4\n1 3 5 7 9\n6 4 2 8"
        d = Query(test)
        self.assertEqual(d.n, 5)
        self.assertEqual(d.m, 4)

        self.assertEqual(Query(test).calculate(), "3 2 1 4")

        test = "5 5\n1 2 1 2 5\n3 1 4 1 5"
        self.assertEqual(Query(test).calculate(), "4 2 4 2 5")

        test = ""

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
        d = Query(test)
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

    sys.stdout.write(Query().calculate())


__starting_point()
