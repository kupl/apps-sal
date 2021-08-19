"""
Please help Haruhi solve this problem.

Input

The first line of input will be a single string s (1<=|s|<=20).
String s consists only of lowercase English letters.

Output

Output a single integer equal to the number of distinct photobooks
Kyoya Ootori can make.

"""
import unittest
import sys
import re


class Photo:
    """ Photo representation """

    def __init__(self, args):
        """ Default constructor """
        self.args = args
        self.str = args

    def calculate(self):
        """ Main calcualtion function of the class """
        result = 0
        for n in range(len(self.str) + 1):
            if n == 0:
                result += 1
            result += 25
        return result


def decode_inputs(inputs):
    """ Decoding input string list into base class args list """
    ilist = inputs[0]
    return ilist


def calculate(inputs):
    """ Base class calculate method wrapper """
    return Photo(decode_inputs(inputs)).calculate()


def main():
    """ Main function. Not called by unit tests """
    inputs = [input()]
    print(calculate(inputs))


class unitTests(unittest.TestCase):

    def test_decode_inputs(self):
        """ Input string decoding testing """
        self.assertEqual(decode_inputs(['a']), 'a')

    def test_Photo_class__basic_functions(self):
        """ Photo class basic functions testing """
        d = Photo('a')
        self.assertEqual(d.str, 'a')

    def test_calculate(self):
        """ Main calculation function """
        self.assertEqual(calculate(['a']), 51)
        self.assertEqual(calculate(['hi']), 76)


def __starting_point():
    if sys.argv[-1] == '-ut':
        unittest.main(argv=[' '])
    main()


__starting_point()
