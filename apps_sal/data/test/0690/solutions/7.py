"""
Created on Nov 11, 2013

@author: Ismael
"""
import sys


def printDigitSoroban(digit):
    if digit == 0:
        print('O-|-OOOO')
    elif digit == 1:
        print('O-|O-OOO')
    elif digit == 2:
        print('O-|OO-OO')
    elif digit == 3:
        print('O-|OOO-O')
    elif digit == 4:
        print('O-|OOOO-')
    elif digit == 5:
        print('-O|-OOOO')
    elif digit == 6:
        print('-O|O-OOO')
    elif digit == 7:
        print('-O|OO-OO')
    elif digit == 8:
        print('-O|OOO-O')
    elif digit == 9:
        print('-O|OOOO-')


def convert(x):
    if x == 0:
        printDigitSoroban(0)
    while x >= 1:
        digit = x % 10
        printDigitSoroban(digit)
        x //= 10


def main():
    f = sys.stdin
    n = int(f.readline())
    convert(n)


main()
