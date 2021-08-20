n = int(input())
arr = [list(map(int, input().split())) for _ in range(n - 1)]
mod = 10 ** 9 + 7
graph = [[] for _ in range(n)]
for (a, b) in arr:
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
parents = [-1] * n
children = [[] for _ in range(n)]
flags = [True] * n
flags[0] = False
stack = [0]
orders = []
while stack:
    index = stack.pop()
    orders.append(index)
    for child in graph[index]:
        if flags[child]:
            parents[child] = index
            children[index].append(child)
            flags[child] = False
            stack.append(child)
fac = [1] * (n + 10)
inv = [1] * (n + 10)
ifac = [1] * (n + 10)
for i in range(2, n + 10):
    fac[i] = fac[i - 1] * i % mod
    inv[i] = -(inv[mod % i] * (mod // i)) % mod
    ifac[i] = ifac[i - 1] * inv[i] % mod
size = [1] * n
dp = [1] * n
for parent in orders[::-1]:
    for child in children[parent]:
        size[parent] += size[child]
        dp[parent] = dp[parent] * dp[child] * ifac[size[child]] % mod
    dp[parent] = dp[parent] * fac[size[parent] - 1] % mod
size2 = [n - i + 1 for i in size]
dp2 = [1] * n
for parent in orders[1:]:
    child = parents[parent]
    dp2[parent] = dp2[parent] * fac[size2[parent] - 2] * dp[child] * dp2[child] * fac[size[parent]] * ifac[size2[child] - 1] * ifac[size[child] - 1] * pow(dp[parent], mod - 2, mod) % mod
for i in range(n):
    print(fac[n - 1] * ifac[size[i] - 1] * ifac[size2[i] - 1] * dp[i] * dp2[i] % mod)
