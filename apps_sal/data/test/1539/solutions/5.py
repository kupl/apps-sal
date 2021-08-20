"""
Input

The first line of the input contains integer n  the initial number of legs
in the table Arthur bought.

The second line of the input contains a sequence of n integers li, where
li is equal to the length of the i-th leg of the table.

The third line of the input contains a sequence of n integers di, where di
is the number of energy units that Arthur spends on removing the i-th leg
off the table.
Output

Print a single integer the minimum number of energy units that Arthur
needs to spend in order to make the table stable.
"""
import unittest
import sys
import re
import random
import bisect


class Table:
    """ Table representation """
    LIM = 201

    def __init__(self, args):
        """ Default constructor """
        self.legs = args[0]
        self.energy = args[1]
        self.n = len(self.legs)
        self.srt = sorted(((l, e) for (l, e) in zip(self.legs, self.energy)))
        self.legs = []
        self.energy = []
        for n in self.srt:
            self.legs.append(n[0])
            self.energy.append(n[1])
        self.itot = 0
        self.ieltot = [0 for i in range(self.LIM)]
        self.ielprev = [0 for i in range(self.LIM)]
        self.ielprev_eng = 0
        self.ires_eng = sys.maxsize

    def get_new_layer_info(self, legs, energy):
        ll = len(legs)
        for (i, l) in enumerate(legs):
            self.ilen = l
            e = energy[i]
            if i == 0:
                self.itop_eng = sum(energy)
            if i == 0 or self.ilen != prev:
                self.irep = 0
                self.ielsum_eng = 0
                self.ielprev = list(self.ieltot)
            self.irep += 1
            self.itop_eng -= e
            self.ielprev_eng += e
            self.ielsum_eng += e
            self.ieltot[e] += 1
            if i == ll - 1 or legs[i + 1] != self.ilen:
                self.irem = self.irep - 1
                self.irem_eng = self.ielprev_eng - self.ielsum_eng
                if self.irem != 0:
                    sumh = self.energyl_sum_high(self.ielprev, self.irem)
                    self.irem_eng -= sumh
                summ = self.itop_eng + self.irem_eng
                self.ires_eng = min(self.ires_eng, summ)
                yield
            prev = self.ilen

    def energyl_sum_high(self, l, n):
        result = 0
        for i in range(len(l) - 1, -1, -1):
            e = l[i]
            if e == 0:
                continue
            if n <= 0:
                break
            result += i * (n if e > n else e)
            n -= e
        return result

    def calculate(self):
        """ Main calcualtion function of the class """
        iter = self.get_new_layer_info(self.legs, self.energy)
        for g in iter:
            pass
        result = self.ires_eng
        return str(result)


def get_inputs(test_inputs=None):
    it = iter(test_inputs.split('\n')) if test_inputs else None

    def uinput():
        """ Unit-testable input function wrapper """
        if it:
            return next(it)
        else:
            return input()
    num = int(uinput())
    str1 = [int(s) for s in uinput().split()]
    str2 = [int(s) for s in uinput().split()]
    inputs = []
    inputs.append(str1)
    inputs.append(str2)
    return inputs


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Table(get_inputs(test_inputs)).calculate()


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add 
 to separate lines """
        imax = 100000
        test = '0\n'
        for i in range(imax):
            test += str(i) + ' '
        test += '\n'
        for i in range(imax):
            test += str(random.randint(1, 200)) + ' '
        calculate(test)
        test = '2\n1 5\n3 2'
        self.assertEqual(calculate(test), '2')
        self.assertEqual(get_inputs(test), [[1, 5], [3, 2]])
        test = '3\n2 4 4\n1 1 1'
        self.assertEqual(calculate(test), '0')
        test = '6\n2 2 1 1 3 3\n4 3 5 5 2 1'
        self.assertEqual(calculate(test), '8')
        test = '10\n20 1 15 17 11 2 15 3 16 3\n' + '129 114 183 94 169 16 18 104 49 146'
        self.assertEqual(calculate(test), '652')

    def test_Table_class__basic_functions(self):
        """ Table class basic functions testing """
        d = Table([[2, 2, 1, 1, 3, 3], [2, 2, 3, 3, 1, 1]])
        self.assertEqual(d.legs[0], 1)
        self.assertEqual(d.energy[0], 3)
        iter = d.get_new_layer_info([1, 1, 2, 2, 4, 5], [2, 2, 3, 3, 1, 1])
        next(iter)
        self.assertEqual(d.itop_eng, 8)
        self.assertEqual(d.ilen, 1)
        self.assertEqual(d.irep, 2)
        self.assertEqual(d.irem, 1)
        self.assertEqual(d.irem_eng, 0)
        self.assertEqual(d.ires_eng, 8)
        next(iter)
        self.assertEqual(d.ilen, 2)
        self.assertEqual(d.irep, 2)
        self.assertEqual(d.irem, 1)
        self.assertEqual(d.irem_eng, 2)
        self.assertEqual(d.ires_eng, 4)
        d = Table([[], []])
        iter = d.get_new_layer_info([1, 1, 2, 2, 3, 3], [5, 5, 4, 3, 2, 1])
        next(iter)
        self.assertEqual(d.ilen, 1)
        self.assertEqual(d.irep, 2)
        self.assertEqual(d.irem, 1)
        self.assertEqual(d.irem_eng, 0)
        self.assertEqual(d.ires_eng, 10)
        next(iter)
        self.assertEqual(d.ilen, 2)
        self.assertEqual(d.irep, 2)
        self.assertEqual(d.irem, 1)
        self.assertEqual(d.irem_eng, 5)
        self.assertEqual(d.ires_eng, 8)
        next(iter)
        self.assertEqual(d.ilen, 3)
        self.assertEqual(d.irep, 2)
        self.assertEqual(d.irem, 1)
        self.assertEqual(d.irem_eng, 12)
        self.assertEqual(d.ires_eng, 8)


def __starting_point():
    sys.setrecursionlimit(100000)
    if sys.argv[-1] == '-ut':
        unittest.main(argv=[' '])
    print(calculate())


__starting_point()
