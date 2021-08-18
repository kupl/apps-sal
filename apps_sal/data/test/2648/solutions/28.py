from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini] * i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini] * i for _ in range(j)] for _ in range(k)]


N = ii()
A = li()

d = defaultdict(int)
for num in A:
    d[num] += 1

flag = 0
cnt = 0
for key, value in d.items():
    if value > 1:
        flag = (flag + value - 1) % 2
    cnt += 1

print(cnt - flag)
