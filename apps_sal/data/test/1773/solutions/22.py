"""
Input

The first line contains one number n (1 n 100), the number of apple trees
in Lala Land.

The following n lines contains two integers each xi, ai, representing the
position of the ith tree and number of apples on it.

It's guaranteed that there is at most one apple tree at each coordinate.
It's guaranteed that no tree grows in point 0.
Output

Output the maximum number of apples Amr can collect.
"""
import unittest
import sys
import re
import random
import bisect
import array


class Apple:
    """ Apple representation """

    def __init__(self, args):
        """ Default constructor """
        self.gn = args[0]
        self.list = args[1]
        self.ploc = []
        self.nloc = []
        for i in range(0, len(self.list), 2):
            loc = (self.list[i], self.list[i + 1])
            if self.list[i] > 0:
                self.ploc.append(loc)
            else:
                self.nloc.append(loc)
        self.ploc1 = list(reversed(sorted(self.ploc)))
        self.nloc1 = list(sorted(self.nloc))
        self.ploc2 = list(self.ploc1)
        self.nloc2 = list(self.nloc1)
        self.tot1 = self.tot(1, self.ploc1, self.nloc1)
        self.tot2 = self.tot(0, self.ploc2, self.nloc2)

    def tot(self, dir, ploc, nloc):
        result = 0
        while True:
            if dir:
                if len(ploc) == 0:
                    break
                result += ploc.pop()[1]
                if len(self.nloc) == 0:
                    break
            else:
                if len(nloc) == 0:
                    break
                result += nloc.pop()[1]
                if len(ploc) == 0:
                    break
            dir = 0 if dir == 1 else 1
        return result

    def calculate(self):
        """ Main calcualtion function of the class """
        result = max(self.tot1, self.tot2)
        return str(result)


def get_inputs(test_inputs=None):
    it = iter(test_inputs.split('\n')) if test_inputs else None

    def uinput():
        """ Unit-testable input function wrapper """
        if it:
            return next(it)
        else:
            return sys.stdin.readline()
    num = int(uinput())
    s = ' '.join((uinput() for i in range(num)))
    numa = list(map(int, s.split()))
    return [num, numa]


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Apple(get_inputs(test_inputs)).calculate()


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add 
 to separate lines """
        test = '2\n-1 5\n1 5'
        self.assertEqual(calculate(test), '10')
        self.assertEqual(get_inputs(test)[0], 2)
        self.assertEqual(list(get_inputs(test)[1]), [-1, 5, 1, 5])
        test = '3\n-2 2\n1 4\n-1 3'
        self.assertEqual(calculate(test), '9')
        test = '3\n1 9\n3 5\n7 10'
        self.assertEqual(calculate(test), '9')
        test = '3\n-1 9\n-3 5\n-7 10'
        self.assertEqual(calculate(test), '9')
        imax = 100
        test = str(imax) + '\n'
        s = (str(i - 100) + ' ' + str(i + 1 - 100) for i in range(imax))
        test += '\n'.join(s)
        self.assertEqual(calculate(test), '0')

    def test_Apple_class__basic_functions(self):
        """ Apple class basic functions testing """
        d = Apple([2, [-1, 5, 1, 5]])
        self.assertEqual(d.list[0], -1)
        self.assertEqual(d.nloc[0], (-1, 5))


def __starting_point():
    sys.setrecursionlimit(100000)
    if sys.argv[-1] == '-ut':
        unittest.main(argv=[' '])
    sys.stdout.write(calculate())


__starting_point()
