import numpy as np
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N + 1)]  # parent to child
for i, p in enumerate(input().split(), 2):
    graph[int(p)].append(i)
X = [None] + [int(x) for x in input().split()]


def dfs(v):
    # None または 白、黒の2つ組を返す
    child = []
    for w in graph[v]:
        c = dfs(w)
        if c is None:
            return None
        child.append(c)
    S = sum(a + b for a, b in child)
    x = X[v]
    dp = np.zeros(x + 1, dtype=np.bool)  # 2択の繰り返しで作れる和
    dp[0] = 1
    for a, b in child:
        prev = dp
        dp = np.zeros_like(prev)
        if a <= x:
            dp[a:] = prev[:x + 1 - a]
        if b <= x:
            dp[b:] |= prev[:x + 1 - b]
    nz = np.nonzero(dp)[0]
    if len(nz) == 0:
        return None
    return x, S - nz[-1]


answer = 'POSSIBLE' if dfs(1) is not None else 'IMPOSSIBLE'
print(answer)
