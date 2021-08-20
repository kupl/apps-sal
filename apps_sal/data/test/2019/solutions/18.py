from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict as dd, Counter
from math import ceil
from math import gcd
import sys
INF = 10 ** 20
MOD = 10 ** 9 + 7


def I():
    return list(map(int, input().split()))


'\nFacts and Data representation\nConstructive? Top bottom up down\n'


def solve():
    s = input()
    stack = []
    cnt = 0
    for i in range(len(s)):
        if stack and stack[-1] != s[i]:
            cnt += 1
            stack.pop()
            continue
        stack.append(s[i])
    if cnt % 2:
        print('DA')
    else:
        print('NET')


(t,) = I()
while t:
    t -= 1
    solve()
