# coding: utf-8





import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect

def main():
    n, m = list(map(int, input().split(" ")))
    for i in range(n):
        a = input().split(" ")
        if "C" in a or "M" in a or "Y" in a:
            print("#Color")
            return
    print("#Black&White")

main()

