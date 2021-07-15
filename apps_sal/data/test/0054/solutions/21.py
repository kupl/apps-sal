#!/usr/bin/env python
# scales.py - Codeforces 552C quiz
#
# Copyright (C) 2015 Sergey
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Vanya has a scales for weighing loads and weights of masses w0,?w1,?w2,?..
.,?w100 grams where w is some integer not less than 2 (exactly one weight
of each nominal value). Vanya wonders whether he can weight an item with mass
m using the given weights, if the weights can be put on both pans of the
scales. Formally speaking, your task is to determine whether it is possible
to place an item of mass m and some weights on the left pan of the scales,
and some weights on the right pan of the scales so that the pans of the scales
were in balance.

Input

The first line contains two integers w,?m (2<=w<=10^9, 1<=m<=10^9) - the
number defining the masses of the weights and the mass of the item.

Output

Print word 'YES' if the item can be weighted and 'NO' if it cannot.
"""

# Standard libraries
import unittest
import sys
import re

# Additional libraries


###############################################################################
# Scales Class
###############################################################################


class Scales:
    """ Scales representation """

    N = 100

    def __init__(self, args):
        """ Default constructor """

        self.args = args
        self.w = args[0]
        self.m = args[1]

        # Iterator starting position
        self.maxwp = self.calc_maxwp()
        self.it_min = 0
        self.it_max = int(3 ** (self.maxwp + 1)) - 1

        self.yes = 0

    def calc_maxwp(self):
        """ Max weight power """
        for p in range(self.N+1):
            if self.w ** p > self.m:
                return p

    def list2dec(self, it):
        result = 0
        for (n, i) in enumerate(it):
            result += i * int(3 ** n)
        return result

    def dec2list(self, dec):
        result = []
        remainder = dec
        for n in range(self.maxwp + 1):
            pow = int(3 ** (self.maxwp - n))
            div = remainder // pow
            remainder -= div * pow
            result.insert(0, div)
        return result

    def step(self):
        """ Step to the next iteration """
        mid = (self.it_max + self.it_min)//2

        if mid in (self.it_max, self.it_min):
            return 0

        w = self.calc_weight(mid)
        if w > self.m:
            self.it_max = mid
        elif w < self.m:
            self.it_min = mid
        else:
            self.yes = 1
            return 0

        return 1

    def calc_weight(self, dec):
        result = 0
        it = self.dec2list(dec)
        for i in range(len(it)):
            s = it[i]
            w = self.w ** i
            if s == 2:
                result += w
            if s == 0:
                result -= w
        return result

    def calculate(self):
        """ Main calcualtion function of the class """

        while self.step():
            pass

        return "YES" if self.yes else "NO"

###############################################################################
# Executable code
###############################################################################


def decode_inputs(inputs):
    """ Decoding input string list into base class args list """

    # Decoding input into a list of integers
    ilist = [int(i) for i in inputs[0].split()]

    return ilist


def calculate(inputs):
    """ Base class calculate method wrapper """
    return Scales(decode_inputs(inputs)).calculate()


def main():
    """ Main function. Not called by unit tests """

    # Read test input string list
    inputs = [input()]

    # Print the result
    print(calculate(inputs))

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_decode_inputs(self):
        """ Input string decoding testing """
        self.assertEqual(decode_inputs(["2 5"]), [2, 5])

    def test_Scales_class__basic_functions(self):
        """ Scales class basic functions testing """
        d = Scales([3, 7])
        self.assertEqual(d.w, 3)
        self.assertEqual(d.m, 7)

        # Find the maximum size (power) of the weight we are need
        self.assertEqual(d.maxwp, 2)

        # Base 3 Iterator value, digits: 0 - -, 1 - 0, 2 - "+"
        self.assertEqual(d.list2dec([1, 0, 2]), 19)
        self.assertEqual(d.dec2list(19), [1, 0, 2])

        # Check starting iterator
        d = Scales([2, 3])
        self.assertEqual(d.it_min, 0)
        self.assertEqual(d.it_max, 26)

        # Step function 1 - success, 0 - final step
        d = Scales([2, 3])
        self.assertEqual(d.step(), 1)
        self.assertEqual(d.it_min, 13)
        self.assertEqual(d.it_max, 26)

        # Weight from the iterator
        d = Scales([3, 7])
        self.assertEqual(d.calc_weight(d.list2dec([0, 1, 2])), 8)

    def test_calculate(self):
        """ Main calculation function """

        # Sample test 1
        self.assertEqual(calculate(["3 7"]), "YES")

        # Sample test 1
        self.assertEqual(calculate(["100 99"]), "YES")

        # Sample test 1
        self.assertEqual(calculate(["2 92600"]), "YES")

def __starting_point():
    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])
    main()

__starting_point()
