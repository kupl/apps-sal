import sys
import math
import queue
sys.setrecursionlimit(1000000)

ans = []


def solve(x):
    if sorted(x) == x:
        ans.append(len(x))
    else:
        solve(x[:len(x) // 2])
        solve(x[len(x) // 2:])


n = int(input())
a = list(map(int, input().split()))

solve(a)
print(max(ans))
