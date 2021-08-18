import sys
import math
mod = 10**9 + 7
md = 998244353
def input(): return sys.stdin.readline().strip()


def inp(): return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    t = 4 * n
    for i in range(n):
        print(t, end=" ")
        t -= 2
    print()
