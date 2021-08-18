
"""
Gerald asks whether it is possible to place the paintings on the board,
or is the board he bought not large enough?
Input

The first line contains two space-separated numbers a1 and b1 the sides
of the board. Next two lines contain numbers a2 b2 a3 and b3 the sides
of the paintings. All numbers ai,?bi in the input are integers and fit into
the range from 1 to 1000.

Output

If the paintings can be placed on the wall, print "YES" (without the quotes),
and if they cannot, print "NO" (without the quotes).
"""

import unittest
import sys


class Art:
    """ Art representation """

    def __init__(self, args):
        """ Default constructor """

        self.numa, self.numb = args

        self.r = self.rect(self.numa[0], self.numb[0])
        self.rmax = self.rect(self.numa[1], self.numb[1])
        self.rmin = self.rect(self.numa[2], self.numb[2])
        if self.rmax[0] < self.rmax[1]:
            self.rmax, self.rmin = self.rmin, self.rmax

        self.remain = []
        if self.rmax[0] < self.r[0] and self.rmax[1] <= self.r[1]:
            self.remain.append((self.r[0] - self.rmax[0], self.r[1]))
        if self.rmax[1] < self.r[1] and self.rmax[0] <= self.r[0]:
            self.remain.append((self.r[0], self.r[1] - self.rmax[1]))

        if self.rmax[1] < self.r[0] and self.rmax[0] <= self.r[1]:
            self.remain.append((self.r[0] - self.rmax[1], self.r[1]))
        if self.rmax[0] < self.r[1] and self.rmax[1] <= self.r[0]:
            self.remain.append((self.r[0], self.r[1] - self.rmax[0]))

    def rect(self, a, b):
        if a > b:
            return (a, b)
        else:
            return (b, a)

    def calculate(self):
        """ Main calcualtion function of the class """

        for rec in self.remain:
            if self.rmin[0] <= rec[0] and self.rmin[1] <= rec[1]:
                return "YES"
            if self.rmin[1] <= rec[0] and self.rmin[0] <= rec[1]:
                return "YES"
        return "NO"


def get_inputs(test_inputs=None):

    it = iter(test_inputs.split("\n")) if test_inputs else None

    def uinput():
        """ Unit-testable input function wrapper """
        if it:
            return next(it)
        else:
            return sys.stdin.readline()

    imax = 3
    numnums = list(map(int, " ".join(uinput() for i in range(imax)).split()))

    numa = []
    numb = []
    for i in range(0, 2 * imax, 2):
        numa.append(numnums[i])
        numb.append(numnums[i + 1])

    return [numa, numb]


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Art(get_inputs(test_inputs)).calculate()


class unitTests(unittest.TestCase):

    def test_Art_class__basic_functions(self):
        """ Art class basic functions testing """

        d = Art([[3, 1, 2], [2, 3, 1]])
        self.assertEqual(d.numa[0], 3)

        self.assertEqual(d.r, (3, 2))
        self.assertEqual(d.rmax, (3, 1))
        self.assertEqual(d.rmin, (2, 1))

        self.assertEqual(d.remain, [(3, 1)])

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        test = "3 2\n1 3\n2 1"
        self.assertEqual(calculate(test), "YES")
        self.assertEqual(list(get_inputs(test)[0]), [3, 1, 2])
        self.assertEqual(list(get_inputs(test)[1]), [2, 3, 1])

        test = "5 5\n3 3\n3 3"
        self.assertEqual(calculate(test), "NO")

        test = "4 2\n2 3\n1 2"
        self.assertEqual(calculate(test), "YES")

        test = "5 5\n1 5\n1 5"
        self.assertEqual(calculate(test), "YES")

    def test_time_limit_test(self):
        """ Quiz time limit test """

        import random

        test = "1000 1000"
        test += "\n900 900"
        test += "\n50 50"

        import timeit

        start = timeit.default_timer()
        args = get_inputs(test)

        init = timeit.default_timer()
        d = Art(args)

        calc = timeit.default_timer()
        d.calculate()

        stop = timeit.default_timer()
        print((
            "\nTime Test: "
            + "{0:.3f}s (inp {1:.3f}s init {2:.3f}s calc {3:.3f}s)".
            format(stop - start, init - start, calc - init, stop - calc)))


def __starting_point():

    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    sys.stdout.write(calculate())


__starting_point()
