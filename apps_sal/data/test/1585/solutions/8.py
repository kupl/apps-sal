import sys
from math import floor
from fractions import Fraction
from decimal import Decimal
from collections import Counter
import itertools

def input(): return sys.stdin.readline().strip()
sys.setrecursionlimit(250000)
def getInt(): return int(input())
def getMultiInt(): return map(int, input().split())
def getIntList(): return list(map(int, input().split()))
def getStr(): return input()
def getMultiStr(): return map(str, input().split())
def getStrList(): return list(map(str, input().split()))

def main():
    x,y = getMultiInt()

    count = 1

    while True:
        if x*2 <=y :
            x = x*2
            count +=1
        else:
            break
    print(count)
def __starting_point():
    main()
__starting_point()
