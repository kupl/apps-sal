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


C = Factorial(N + 1, MOD)

G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

order = []
order_append = order.append

stack = [(0, -1)]
stack_pop = stack.pop
stack_append = stack.append

while stack:
    tmp = stack_pop()
    order_append(tmp)
    for next_ in G[tmp[0]]:
        if next_ == tmp[1]:
            continue
        stack_append((next_, tmp[0]))

size = [1] * N
dp = [1] * N

# print (order)
for c, p in order[::-1]:
    if c == 0:
        break
    size[p] += size[c]

for c, p in order[::-1]:
    dp[c] = (dp[c] * C.factorial(size[c] - 1)) % MOD
    if c == 0:
        break
    # dp[c] = (dp[c] * C.factorial(size[c] - 1)) % MOD
    dp[p] = (dp[p] * dp[c] % MOD) * C.ifactorial(size[c]) % MOD

# print (dp)
dp2 = [0] * N
dp2[0] = dp[0]

for c, p in order[1::]:
    tmp = (dp2[p] * C.factorial(N - 1 - size[c]) % MOD) * C.factorial(size[c]) % MOD
    red = (tmp * C.ifactorial(N - 1) % MOD) * pow(dp[c], MOD - 2, MOD) % MOD

    size_red = N - size[c]
    tmp = (dp[c] * red % MOD) * C.factorial(N - 1) % MOD
    dp2[c] = (tmp * C.ifactorial(size[c] - 1) % MOD) * C.ifactorial(size_red) % MOD


print(*dp2, sep='\n')
