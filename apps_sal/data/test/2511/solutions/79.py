from collections import deque
import sys
input = sys.stdin.readline


class Modinv:
    def __init__(self, n, mod):
        self.mod = mod
        self.fact = [1] * n
        self.finv = [1] * n
        self.inv = [1] * n
        for i in range(2, n):
            self.fact[i] = (self.fact[i - 1] * i) % self.mod
            self.inv[i] = self.mod - self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.finv[i] = self.finv[i - 1] * self.inv[i] % self.mod

    def nCr(self, n, r):
        if n < r:
            return 0
        else:
            return self.fact[n] * (self.finv[r] * self.finv[n - r] % self.mod) % self.mod

    def nPr(self, n, r):
        if n < r:
            return 0
        else:
            return self.fact[n] * self.finv[n - r] % self.mod


mod = 10**9 + 7

N, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N - 1)]

A = [[] for _ in range(N)]
for a, b in AB:
    A[a - 1].append(b - 1)
    A[b - 1].append(a - 1)

Modinv = Modinv(K + 10, mod)

ans = K

dq = deque([(0, 0)])
visited = [False] * N

while dq:
    v, d = dq.pop()
    visited[v] = True
    cnt = 0
    for e in A[v]:
        if visited[e]:
            continue
        cnt += 1
        dq.append((e, d + 1))
    if cnt == 0:
        continue
    if d == 0:
        n = Modinv.nPr(K - 1, cnt)
    else:
        n = Modinv.nPr(K - 2, cnt)

    ans *= n
    ans %= mod

print(ans)
