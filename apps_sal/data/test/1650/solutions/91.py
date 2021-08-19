from collections import deque
import bisect
import math
import sys
sys.setrecursionlimit(10000000)


def input():
    return sys.stdin.readline()[:-1]


l = input()
mod = 10 ** 9 + 7
l = deque(l)


def llo(st):
    if len(st) == 1 and st[0] == '0':
        return 1
    elif len(st) == 1 and st[0] == '1':
        return 3
    tmp = st.popleft()
    if tmp == '0':
        return llo(st)
    else:
        return (pow(3, len(st), mod) + 2 * llo(st)) % mod


if '0' not in l:
    print(pow(3, len(l), mod))
else:
    ans = llo(l)
    print(ans)
