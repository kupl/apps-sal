import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7


class Factorial:

    def __init__(self, n, mod):
        self.f = [1]
        self.mod = mod
        for j in range(1, n + 1):
            self.f.append(self.f[-1] * j % mod)
        self.i = [pow(self.f[-1], mod - 2, mod)]
        for j in range(n, 0, -1):
            self.i.append(self.i[-1] * j % mod)
        self.i.reverse()

    def factorial(self, j):
        return self.f[j]

    def ifactorial(self, j):
        return self.i[j]

    def comb(self, n, k):
        return self.f[n] * self.i[n - k] % self.mod * self.i[k] % self.mod if n >= k else 0


N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    (a, b) = list(map(int, input().split()))
    G[a].append(b)
    G[b].append(a)
F = Factorial(N + 2, MOD)
root = 1
stack = [root]
check = [False] * (N + 1)
check[root] = True
p = [0] * (N + 1)
DAG = []
while stack:
    now_ = stack.pop()
    DAG.append(now_)
    for next_ in G[now_]:
        if check[next_]:
            continue
        stack.append(next_)
        check[next_] = True
        p[next_] = now_
size1 = [0] * (N + 1)
dp1 = [1] * (N + 1)
for now_ in DAG[::-1]:
    size1[now_] += 1
    size1[p[now_]] += size1[now_]
    dp1[now_] *= F.factorial(size1[now_] - 1)
    dp1[now_] %= MOD
    dp1[p[now_]] *= dp1[now_] * F.ifactorial(size1[now_])
    dp1[p[now_]] %= MOD
size2 = [N - size1[i] + 1 for i in range(N + 1)]
dp2 = [1] * (N + 1)
for i in DAG:
    parent = i
    for now_ in G[i]:
        if now_ == p[i]:
            continue
        x = dp1[parent]
        x *= F.ifactorial(size1[parent] - 1)
        x *= F.factorial(size1[now_])
        x *= pow(dp1[now_], MOD - 2, MOD)
        x *= dp2[parent]
        x *= F.ifactorial(size2[parent] - 1)
        x *= F.factorial(size2[now_] - 2)
        dp2[now_] = x % MOD
for i in range(1, N + 1):
    ans = dp1[i] * F.ifactorial(size1[i] - 1) * dp2[i] * F.ifactorial(size2[i] - 1) * F.factorial(N - 1)
    print(ans % MOD)
