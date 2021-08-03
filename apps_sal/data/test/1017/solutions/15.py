#!/usr/bin/env python3
# 669A_presents.py - Codeforces.com/problemset/problem/669/A by Sergey 2016

import unittest
import sys

###############################################################################
# Presents Class (Main Program)
###############################################################################


class Presents:
    """ Presents representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """

        result = (self.n // 3) * 2
        if self.n % 3 != 0:
            result += 1

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Presents class testing """

        # Constructor test
        test = "1"
        d = Presents(test)
        self.assertEqual(d.n, 1)

        # Sample test
        self.assertEqual(Presents(test).calculate(), "1")

        # Sample test
        test = "2"
        self.assertEqual(Presents(test).calculate(), "1")

        # Sample test
        test = "3"
        self.assertEqual(Presents(test).calculate(), "2")

        # My tests
        test = "5"
        self.assertEqual(Presents(test).calculate(), "3")

        # Time limit test
        # self.time_limit_test(5000)

    def time_limit_test(self, nmax):
        """ Timelimit testing """
        import random
        import timeit

        # Random inputs
        test = str(nmax) + " " + str(nmax) + "\n"
        numnums = [str(i) + " " + str(i + 1) for i in range(nmax)]
        test += "\n".join(numnums) + "\n"
        nums = [random.randint(1, 10000) for i in range(nmax)]
        test += " ".join(map(str, nums)) + "\n"

        # Run the test
        start = timeit.default_timer()
        d = Presents(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print(("\nTimelimit Test: "
              + "{0:.3f}s (init {1:.3f}s calc {2:.3f}s)".
               format(stop - start, calc - start, stop - calc)))


def __starting_point():

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(Presents().calculate())


__starting_point()
