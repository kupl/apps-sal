#!/usr/bin/env python3
# 600C_palindrom.py - Codeforces.com/problemset/problem/600/C by Sergey 2015

import unittest
import sys

###############################################################################
# Palindrom Class (Main Program)
###############################################################################


class Palindrom:
    """ Palindrom representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        self.s = uinput()

        self.cnt = [0] * 26
        for c in self.s:
            self.cnt[ord(c) - ord('a')] += 1

        self.hlen = len(self.s) // 2
        self.odd = len(self.s) % 2

        self.pcnt = list(self.cnt)
        for i in range(len(self.pcnt) - 1, -1, -1):
            if self.pcnt[i] % 2:
                self.pcnt[i] -= 1
                found = 0
                for j in range(len(self.pcnt)):
                    if self.pcnt[j] % 2:
                        self.pcnt[j] += 1
                        found = 1
                        break
                if not found:
                    self.pcnt[i] += 1

    def calculate(self):
        """ Main calcualtion function of the class """

        result = []
        mid = ""

        for (i, n) in enumerate(self.pcnt):
            if n > 0:
                c = chr(ord('a') + i)
                for i in range(n // 2):
                    result.append(c)
                if n % 2:
                    mid = c
        if self.odd:
            result += mid
            result += reversed(result[:-1])
        else:
            result += reversed(result)

        return "".join(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Palindrom class testing """

        # Constructor test
        test = "aabc"
        d = Palindrom(test)
        self.assertEqual(d.cnt[:3], [2, 1, 1])
        self.assertEqual(d.pcnt[:3], [2, 2, 0])

        # Sample test
        self.assertEqual(Palindrom(test).calculate(), "abba")

        # Sample test
        test = "aabcd"
        self.assertEqual(Palindrom(test).calculate(), "abcba")

        # Sample test
        test = "aabbcccdd"
        self.assertEqual(Palindrom(test).calculate(), "abcdcdcba")

        # My tests
        test = ""
        # self.assertEqual(Palindrom(test).calculate(), "0")

        # Time limit test
        # self.time_limit_test(5000)

    def time_limit_test(self, nmax):
        """ Timelimit testing """
        import random
        import timeit

        # Random inputs
        test = str(nmax) + " " + str(nmax) + "\n"
        numnums = [str(i) + " " + str(i+1) for i in range(nmax)]
        test += "\n".join(numnums) + "\n"
        nums = [random.randint(1, 10000) for i in range(nmax)]
        test += " ".join(map(str, nums)) + "\n"

        # Run the test
        start = timeit.default_timer()
        d = Palindrom(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print(("\nTimelimit Test: " +
              "{0:.3f}s (init {1:.3f}s calc {2:.3f}s)".
              format(stop-start, calc-start, stop-calc)))

def __starting_point():

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(Palindrom().calculate())

__starting_point()
