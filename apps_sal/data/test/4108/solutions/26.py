import bisect
import collections
import copy
import itertools
import math
import string
import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def main():
    s = S()
    t = S()
    dic1 = collections.defaultdict(str)
    dic2 = collections.defaultdict(str)
    for i in range(len(s)):
        if dic1[t[i]] == '':
            dic1[t[i]] = s[i]
        elif dic1[t[i]] != s[i]:
            print('No')
            return
        if dic2[s[i]] == '':
            dic2[s[i]] = t[i]
        elif dic2[s[i]] != t[i]:
            print('No')
            return
    print('Yes')


main()
