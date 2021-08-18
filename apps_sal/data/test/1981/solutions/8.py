
import unittest
import sys
import collections


class Node:

    def __init__(self, i, n):
        self.i = i
        self.n = n
        self.children = []
        self.edges = []
        self.parent = -1

    def add_child(self, c):
        c.parent = self
        self.children.append(c)

    def add_edge(self, e):
        e.edges.append(self)
        self.edges.append(e)


class Park:
    """ Park representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        [self.n, self.m] = list(map(int, uinput().split()))

        self.nums = list(map(int, uinput().split()))

        l, s = self.n - 1, 2
        inp = (" ".join(uinput() for i in range(l))).split()
        self.numm = [[int(inp[i]) for i in range(j, l * s, s)] for j in range(s)]
        self.numa, self.numb = self.numm

        self.nodes = [Node(i, self.nums[i]) for i in range(len(self.nums))]

        for i in range(len(self.numa)):
            self.nodes[self.numa[i] - 1].add_edge(self.nodes[self.numb[i] - 1])

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0

        d = collections.deque([self.nodes[0]])
        visited = set()
        while d:
            v = d.pop()
            visited.add(v.i)
            for e in v.edges:
                if e.i not in visited:
                    v.add_child(e)
                    d.append(e)

        d = collections.deque([self.nodes[0]])
        while d:
            v = d.pop()
            v.cons = v.n if v.i == 0 else (v.parent.cons + 1 if v.n else 0)
            if v.cons <= self.m:
                d.extend(v.children)
                if not v.children:
                    result += 1

        return str(result)


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Park class testing """

        test = "4 1\n1 1 0 0\n1 2\n1 3\n1 4"
        d = Park(test)
        self.assertEqual(d.n, 4)
        self.assertEqual(d.m, 1)
        self.assertEqual(d.numa, [1, 1, 1])
        self.assertEqual(d.numb, [2, 3, 4])
        self.assertEqual(d.nums, [1, 1, 0, 0])

        self.assertEqual(Park(test).calculate(), "2")

        test = "7 1\n1 0 0 1 0 0 1\n1 2\n1 7\n2 4\n2 5\n6 3\n7 3"
        self.assertEqual(Park(test).calculate(), "2")

        test = "7 1\n0 0 1 1 0 0 1\n1 2\n1 3\n2 4\n2 5\n3 6\n3 7"
        self.assertEqual(Park(test).calculate(), "3")

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
        d = Park(test)
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

    sys.stdout.write(Park().calculate())


__starting_point()
