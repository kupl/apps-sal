#!/usr/bin/env python
# 580C_park.py - Codeforces.com/problemset/problem/580/C by Sergey 2015

import unittest
import sys
import collections

###############################################################################
# Park Class (Main Program)
###############################################################################


class Node:

    def __init__(self, num, is_cat):
        self.num = num
        self.c = is_cat
        self.chs = []
        self.edgs = []

    def add_ch(self, ch):
        ch.parent = self
        self.chs.append(ch)

    def add_edge(self, e):
        e.edgs.append(self)
        self.edgs.append(e)


class Park:
    """ Park representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n, self.m] = list(map(int, uinput().split()))

        # Reading a single line of multiple elements
        self.nums = list(map(int, uinput().split()))

        # Reading multiple lines of pairs
        pairs = (" ".join(uinput() for i in range(self.n - 1))).split()
        self.numa = [int(pairs[i]) for i in range(0, 2 * (self.n - 1), 2)]
        self.numb = [int(pairs[i]) for i in range(1, 2 * (self.n - 1), 2)]

        # Building the tree
        self.nodes = []
        for i in range(self.n):
            self.nodes.append(Node(i, self.nums[i]))

        for i in range(self.n - 1):
            self.nodes[self.numa[i] - 1].add_edge(self.nodes[self.numb[i] - 1])

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0

        # BFS
        d = collections.deque()
        d.append(self.nodes[0])
        vis = set()
        while d:
            v = d.popleft()
            vis.add(v.num)
            for e in v.edgs:
                if e.num not in vis:
                    e.parent = v
                    v.chs.append(e)
                    d.append(e)

        # BFS
        d = collections.deque()
        d.append(self.nodes[0])
        while d:
            v = d.popleft()
            if v.num == 0:
                v.cons = v.c
                v.conssf = v.cons
            else:
                p = v.parent
                if v.c:
                    v.cons = p.cons + 1
                    v.conssf = max(p.conssf, v.cons)
                else:
                    v.cons = 0
                    v.conssf = p.conssf
            d.extend(v.chs)
            if len(v.chs) == 0 and v.conssf <= self.m:
                result += 1

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Park class testing """

        # Constructor test
        test = "4 1\n1 1 0 0\n1 2\n1 3\n1 4"
        d = Park(test)
        self.assertEqual(d.n, 4)
        self.assertEqual(d.m, 1)
        self.assertEqual(d.numa, [1, 1, 1])
        self.assertEqual(d.numb, [2, 3, 4])
        self.assertEqual(d.nums, [1, 1, 0, 0])

        # Sample test
        self.assertEqual(Park(test).calculate(), "2")

        # Sample test
        test = "7 1\n1 0 1 1 0 0 0\n1 2\n1 3\n2 4\n2 5\n3 6\n3 7"
        self.assertEqual(Park(test).calculate(), "2")

        # Sample test
        test = "7 1\n0 0 1 1 0 0 1\n1 2\n1 3\n2 4\n2 5\n3 6\n3 7"
        self.assertEqual(Park(test).calculate(), "3")

        # My tests
        test = ""
        # self.assertEqual(Park(test).calculate(), "0")

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
        d = Park(test)
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
    sys.stdout.write(Park().calculate())


__starting_point()
