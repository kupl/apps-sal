#!/usr/bin/env python3
# 599D_squares.py - Codeforces.com/problemset/problem/599/D by Sergey 2015

import unittest
import sys

###############################################################################
# Squares Class (Main Program)
###############################################################################


class Squares:
    """ Squares representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """

        result = []
        n = 1
        while n * n * (n - 1) // 6 < self.n:
            a = n * (n + 1) // 2
            b = n * (n - 1) * (n + 1) // 6
            m = self.n + b
            k = m // a
            if n <= k and m % a == 0:
                result.append((n, k))
            n += 1
        result2 = list(result)
        result2 += [(b, a) for a, b in reversed(result) if a != b]
        s = str(len(result2)) + "\n"
        s += "\n".join([str(a) + " " + str(b) for a, b in result2])

        return s

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Squares class testing """

        # Constructor test
        test = "26"
        d = Squares(test)
        self.assertEqual(d.n, 26)

        # Sample test
        self.assertEqual(
            Squares(test).calculate(), "6\n1 26\n2 9\n3 5\n5 3\n9 2\n26 1")

        # Sample test
        test = "0"
        self.assertEqual(Squares(test).calculate(), "0\n")

        # Sample test
        test = ""
        # self.assertEqual(Squares(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Squares(test).calculate(), "0")

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
        d = Squares(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print(("\nTimelimit Test: " +
              "{0:.3f}s (init {1:.3f}s calc {2:.3f}s)".
               format(stop - start, calc - start, stop - calc)))


def __starting_point():

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(Squares().calculate())


__starting_point()
