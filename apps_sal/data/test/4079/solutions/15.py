from collections import defaultdict as DD
from bisect import bisect_left as BL
from bisect import bisect_right as BR
from itertools import combinations as IC
from itertools import permutations as IP
from random import randint as RI
import sys
MOD = pow(10, 9) + 7


def IN(f=0):
    if f == 0:
        return ([int(i) for i in sys.stdin.readline().split()])
    else:
        return (int(sys.stdin.readline()))


nn = IN(1)
for _ in range(nn):
    s = input()
    s = list(s)
    s.sort()
    n = len(s)
    if len(set(s)) != n:
        print("No")
    else:
        f = 0
        for i in range(1, n):
            if abs(ord(s[i]) - ord(s[i - 1])) != 1:
                f = 1
        if f == 1:
            print("No")
        else:
            print("Yes")
