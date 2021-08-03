from collections import defaultdict
import sys
import math


def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()


for _ in range(int(input())):
    (n, k) = get_ints()
    a = get_array()
    if len(set(a)) <= k:
        print(1)
        continue
    if k == 1:
        print(-1)
        continue

    l = len(set(a))
    ans = 1
    l -= k
    while(l > 0):
        l -= (k - 1)
        ans += 1
    print(ans)
