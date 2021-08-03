import sys
input = sys.stdin.readline


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


MOD = 10 ** 9 + 7

F = Factorial(2 * 10 ** 5 + 10, MOD)

N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    G[a].append(b)
    G[b].append(a)


root = 1

DAG = []
parent = [-1] * (N + 1)
parent[root] = 0
stack = [root]
while stack:
    now_ = stack.pop()
    DAG.append(now_)
    for next_ in G[now_]:
        if parent[next_] == -1:
            stack.append(next_)
            parent[next_] = now_

# print ('parent', parent)

size1 = [1] * (N + 1)
dp1 = [1] * (N + 1)

for i in DAG[::-1]:
    size1[parent[i]] += size1[i]

for i in DAG[::-1]:
    dp1[i] *= F.factorial(size1[i] - 1)
    dp1[i] %= MOD
    dp1[parent[i]] *= (dp1[i] * F.ifactorial(size1[i])) % MOD
    dp1[parent[i]] %= MOD

# print (dp1)
# print (size1)

size2 = [1] * (N + 1)
dp2 = [1] * (N + 1)

for i in DAG[::]:
    for j in G[i]:
        if parent[i] == j:
            continue
        size2[j] = size2[i] + size1[i] - size1[j]

for i in DAG[1::]:
    x = 1
    x *= dp1[parent[i]]
    x *= F.ifactorial(size1[parent[i]] - 1)
    x *= F.factorial(size1[i])
    x *= pow(dp1[i], MOD - 2, MOD)
    x *= dp2[parent[i]]
    x *= F.ifactorial(size2[parent[i]] - 1)
    x *= F.factorial(size2[i] - 2)
    dp2[i] = x % MOD

# print ('size1', size1)
# print ('size2', size2)
# print ('dp1', dp1)
# print ('dp2', dp2)
# print (G)

fact = F.factorial(N - 1)
for x in range(1, N + 1):
    ans = fact * dp1[x] * F.ifactorial(size1[x] - 1) * dp2[x] * F.ifactorial(size2[x] - 1)
    print((ans % MOD))
