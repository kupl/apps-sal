#!/usr/bin/env python3
import sys
from collections import defaultdict
MOD = 1000000007  # type: int


class Combination(object):

    def __init__(self, N, mod=MOD):
        fac, finv, inv = [0]*(N+1), [0]*(N+1), [0]*(N+1)
        fac[:2] = 1, 1
        finv[:2] = 1, 1
        inv[1] = 1
        for i in range(2, N+1):
            fac[i] = fac[i-1]*i % mod
            inv[i] = -inv[mod % i]*(mod//i) % mod
            finv[i] = finv[i-1]*inv[i] % mod
        self.N = N
        self.MOD = mod
        self.fac = fac
        self.finv = finv
        self.inv = inv

    def __call__(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        b = (self.finv[k]*self.finv[n-k] % self.MOD)
        return (self.fac[n] * b) % self.MOD


def make_downward(E, N, s=0):
    # BFSでdownward順を構成する
    front, back = 0, 1
    downward = [s]*N
    parent = [-1]*N
    for _ in range(N-1):
        v = downward[front]
        front += 1
        for u in E[v]:
            if u == parent[v]:
                continue
            parent[u] = v
            downward[back] = u
            back += 1
    # print(downward)
    return downward, parent


def solve(N: int, a: "List[int]", b: "List[int]"):
    # グラフの構築
    E = [[] for _ in range(N)]
    for aa, bb in zip(a, b):
        E[aa-1].append(bb-1)
        E[bb-1].append(aa-1)

    # 組み合わせの初期化
    cmb = Combination(N)

    # BFSでdownward順を構成する
    downward, parent = make_downward(E, N)

    # 節点vを根とした部分木の塗り方dp[v]
    dp = [1]*N
    # 節点vを根とした部分木のサイズsize[v]+1
    size = [0]*N

    # 木DP
    # 葉から根へ向かう探索
    for v in reversed(downward):
        for u in E[v]:
            if u == parent[v]:
                continue
            size[v] += size[u]+1
            dp[v] *= cmb.finv[size[u]+1]
            dp[v] %= MOD
            dp[v] *= dp[u]
            dp[v] %= MOD
        dp[v] *= cmb.fac[size[v]]
        dp[v] %= MOD

    # 全方位木DP
    # 根から葉へ向かう探索
    for v in downward:
        for u in E[v]:
            if u == parent[v]:
                continue
            dp[u] = dp[v]
            dp[u] *= (size[u]+1)*cmb.inv[N-(size[u]+1)]
            dp[u] %= MOD

    for v in dp:
        print(v)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)


def __starting_point():
    main()

__starting_point()
