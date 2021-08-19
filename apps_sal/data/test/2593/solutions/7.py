# Python template
from collections import defaultdict
import sys
import math


def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def input(): return sys.stdin.readline().strip()


def f(n):
    cnt = 0
    while(n):
        n = n // 2
        cnt += 1
    return cnt


for _ in range(int(input())):
    n = int(input())
    a = get_array()

    d = defaultdict(int)

    for i in range(n):
        d[f(a[i])] += 1

    ans = 0
    for i in list(d.values()):
        ans += (i * (i - 1)) // 2
    print(ans)
