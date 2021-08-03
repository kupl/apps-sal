#!/usr/bin/env python3
# 599C_beach.py - Codeforces.com/problemset/problem/599/C by Sergey 2015

import unittest
import sys

###############################################################################
# Beach Class (Main Program)
###############################################################################


class Beach:
    """ Beach representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = list(map(int, uinput().split()))

        # Reading a single line of multiple elements
        self.nums = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """

        result, u = 0, 0

        tp = sorted([(n, i) for i, n in enumerate(self.nums)])

        for i in range(self.n):
            u = max(u, tp[i][1])
            if i >= u:
                result += 1

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Beach class testing """

        # Constructor test
        test = "3\n1 2 3"
        d = Beach(test)
        self.assertEqual(d.n, 3)
        self.assertEqual(d.nums, [1, 2, 3])

        # Sample test
        self.assertEqual(Beach(test).calculate(), "3")

        # Sample test
        test = "4\n2 1 3 2"
        self.assertEqual(Beach(test).calculate(), "2")

        # My tests
        test = ""
        # self.assertEqual(Beach(test).calculate(), "0")

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
        d = Beach(test)
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
    sys.stdout.write(Beach().calculate())


__starting_point()
