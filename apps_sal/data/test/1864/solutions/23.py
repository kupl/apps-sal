
"""
Input

The first line contains number n the number of values of
the banknotes that used in Geraldion.

The second line contains n distinct space-separated numbers
a1,..an  the values of the banknotes.
Output

Print a single line the minimum unfortunate sum. If there
are no unfortunate sums, print -1.

"""

import unittest
import sys


class Currency:
    """ Currency representation """

    def __init__(self, args):
        """ Default constructor """

        self.imax, self.nums = args

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 1
        for n in self.nums:
            if n == 1:
                result = -1
                break

        return str(result)


def get_inputs(test_inputs=None):

    it = iter(test_inputs.split("\n")) if test_inputs else None

    def uinput():
        """ Unit-testable input function wrapper """
        if it:
            return next(it)
        else:
            return sys.stdin.readline()

    imax = int(uinput())
    nums = list(map(int, uinput().split()))

    return [imax, nums]


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Currency(get_inputs(test_inputs)).calculate()


class unitTests(unittest.TestCase):

    def test_Currency_class__basic_functions(self):
        """ Currency class basic functions testing """

        d = Currency([5, [1, 2, 3, 4, 5]])
        self.assertEqual(d.imax, 5)

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        test = "5\n1 2 3 4 5"
        self.assertEqual(calculate(test), "-1")
        self.assertEqual(get_inputs(test)[0], 5)
        self.assertEqual(list(get_inputs(test)[1]), [1, 2, 3, 4, 5])

        test = "3\n5 6 2"
        self.assertEqual(calculate(test), "1")

        test = "1\n12"

        test = "1\n12"

    def test_time_limit_test(self):
        """ Quiz time limit test """

        import random

        imax = 1000
        num = str(imax)
        test = num + "\n"
        numnums = [str(i) + " " + str(i + 1) for i in range(imax)]
        test += "\n".join(numnums) + "\n"
        nums = [random.randint(1, 10000) for i in range(imax)]
        test += " ".join(map(str, nums)) + "\n"

        import timeit

        start = timeit.default_timer()
        args = get_inputs(test)

        init = timeit.default_timer()
        d = Currency(args)

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
