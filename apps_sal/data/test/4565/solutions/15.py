from itertools import accumulate
import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini] * i for _ in range(j)]


N = ii()
S = input()
cnt = [0] * N

for i in range(N):
    if S[i] == 'W':
        cnt[i] = 1

cnt = list(accumulate(cnt))
ans = N

for i in range(N):
    if S[i] == 'E':
        ans = min(ans, cnt[i] + (N - 1 - i) - (cnt[-1] - cnt[i]))
    else:
        ans = min(ans, i + 1 - cnt[i] + (N - 1 - i) - (cnt[-1] - cnt[i]))

print(ans)
