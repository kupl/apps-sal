from collections import deque
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


N = int(input())

c = Factorial(N + 2, MOD)

G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

edge_num = [len(G[i]) for i in range(N + 1)]

que = deque()
check = [0] * (N + 1)
order = []
o_append = order.append
q_pop = que.pop
q_append = que.append

q_append((1, 0))
check[1] = 1
while que:
    now = q_pop()
    o_append(now)
    for next_ in G[now[0]]:
        if check[next_] == 0:
            q_append((next_, now[0]))
            check[next_] = 1


size1 = [0] * (N + 1)
dp1 = [1] * (N + 1)
for child, parent in order[::-1]:
    dp1[child] *= c.factorial(size1[child])
    dp1[child] %= MOD
    s = size1[child] + 1
    size1[parent] += s
    dp1[parent] *= c.ifactorial(s) * dp1[child]
    dp1[parent] %= MOD


size2 = [N - 2 - x for x in size1]
dp2 = [1] * (N + 1)

for child, parent in order[1:]:
    x = dp1[parent]
    x *= dp2[parent]
    x *= c.ifactorial(size1[parent])
    x *= c.factorial(size1[child] + 1)
    x *= pow(dp1[child], MOD - 2, MOD)
    x *= c.factorial(size2[child])
    x *= c.ifactorial(size2[parent] + 1)
    dp2[child] = x % MOD


for x1, x2, s1, s2 in zip(dp1[1:], dp2[1:], size1[1:], size2[1:]):
    s2 += 1
    x = x1 * x2 * c.factorial(s1 + s2) * c.ifactorial(s1) * c.ifactorial(s2) % MOD
    print(x)
