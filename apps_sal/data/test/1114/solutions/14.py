
import unittest
import sys


class Sponge:
    """ Sponge representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        [self.n, self.m] = list(map(int, uinput().split()))

        self.numf = list(map(int, uinput().split()))

        self.numb = list(map(int, uinput().split()))

        self.fd = {}
        self.fdn = {}
        for (i, n) in enumerate(self.numf):
            self.fd[n] = self.fd.setdefault(n, 0) + 1
            self.fdn[n] = i + 1
        self.bd = {}
        for (i, n) in enumerate(self.numb):
            self.bd[n] = self.bd.setdefault(n, 0) + 1

    def calculate(self):
        """ Main calcualtion function of the class """

        result = []
        for n in self.numb:
            if n not in self.fd:
                return "Impossible"
        for n in self.numb:
            if self.fd[n] > 1:
                return "Ambiguity"
            result.append(self.fdn[n])

        return "Possible\n" + " ".join(map(str, result))


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Sponge class testing """

        test = "3 3\n3 2 1\n1 2 3"
        d = Sponge(test)
        self.assertEqual(d.n, 3)
        self.assertEqual(d.m, 3)
        self.assertEqual(d.numf, [3, 2, 1])
        self.assertEqual(d.numb, [1, 2, 3])

        self.assertEqual(Sponge(test).calculate(), "Possible\n3 2 1")

        test = "3 3\n1 1 3\n1 2"
        self.assertEqual(Sponge(test).calculate(), "Impossible")

        test = "3 3\n1 1 1\n1 1 1"
        self.assertEqual(Sponge(test).calculate(), "Ambiguity")

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
        d = Sponge(test)
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

    sys.stdout.write(Sponge().calculate())


__starting_point()
