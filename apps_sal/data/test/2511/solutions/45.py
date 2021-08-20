from collections import defaultdict
from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
(N, K) = list(map(int, input().split()))
ab = defaultdict(list)
for i in range(N - 1):
    (a, b) = list(map(int, input().split()))
    ab[a - 1].append(b - 1)
    ab[b - 1].append(a - 1)
MOD = 10 ** 9 + 7


def dfs(v, pv, n):
    k = K - 1 if pv == -1 else K - 2
    a = 1
    for u in ab[v]:
        if u != pv:
            a *= dfs(u, v, k)
            a %= MOD
            k -= 1
    return a * n % MOD


print(dfs(0, -1, K))
