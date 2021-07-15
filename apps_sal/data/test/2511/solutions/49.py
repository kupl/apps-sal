# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
graph = [[] for _ in range(N+1)]  # 1-indexed
for _ in range(N-1):
    a, b = lr()
    graph[a].append(b)
    graph[b].append(a)

MOD = 10 ** 9 + 7

def perm(n,k):
    if k > n or k < 0: return 0
    return fact[n] * fact_inv[n-k] % MOD

def cmb(n, k):
    if k < 0 or k > n: return 0
    return fact[n] * fact_inv[k] % MOD * fact_inv[n-k] % MOD

def cumprod(arr, MOD):
    L = len(arr); Lsq = int(L**.5+1)
    arr = np.resize(arr, Lsq**2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n-1]; arr[:, n] %= MOD
    for n in range(1, Lsq):
        arr[n] *= arr[n-1, -1]; arr[n] %= MOD
    return arr.ravel()[:L]

def make_fact(U, MOD):
    x = np.arange(U, dtype=np.int64); x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64); x[0] = pow(int(fact[-1]), MOD-2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact, fact_inv

U = 10 ** 6  # 階乗テーブルの上限
fact, fact_inv = make_fact(U, MOD)
#print(answer % MOD)
# np.int64とint型の違いに注意
answer = 1
root = 1
parent = [0] * (N+1)
order = []
stack = [root]
answer = K * perm(K-1, len(graph[root])) % MOD
while stack:
    cur = stack.pop()
    order.append(cur)
    if cur != 1:
        answer *= perm(K-2, len(graph[cur])-1)
        answer %= MOD
    for next in graph[cur]:
        if next == parent[cur]:
            continue
        parent[next] = cur
        stack.append(next)

print((answer%MOD))

