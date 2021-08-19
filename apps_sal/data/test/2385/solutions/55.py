n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    (a, b) = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
mod = 10 ** 9 + 7
factorial = [1] * (n + 1)
factorial_inv = [1] * (n + 1)
for i in range(1, n + 1):
    factorial[i] = factorial[i - 1] * i % mod
factorial_inv[n] = pow(factorial[n], mod - 2, mod)
for i in range(n, 0, -1):
    factorial_inv[i - 1] = factorial_inv[i] * i % mod
pa = [0] * (n + 1)
dp = [1] * (n + 1)
size = [1] * (n + 1)
checked = []
stack = [i]
while stack:
    a = stack.pop()
    checked.append(a)
    for j in graph[a]:
        if pa[a] == j:
            continue
        else:
            stack.append(j)
            pa[j] = a
for i in checked[::-1]:
    p = pa[i]
    s = size[i]
    dp[i] *= factorial[s - 1]
    dp[i] %= mod
    dp[p] *= dp[i] * factorial_inv[s]
    dp[p] %= mod
    size[p] += s
size_ = [n - i + 1 for i in size]
dp_ = [1] * (n + 1)
for i in checked[1:]:
    p = pa[i]
    dp_[i] *= dp[p]
    dp_[i] *= factorial_inv[size[p] - 1]
    dp_[i] *= pow(dp[i], mod - 2, mod)
    dp_[i] *= factorial[size[i]]
    dp_[i] *= dp_[p]
    dp_[i] *= factorial_inv[size_[p] - 1]
    dp_[i] *= factorial[size_[i] - 2]
    dp_[i] %= mod
for i in range(1, n + 1):
    ans = factorial[n - 1] * dp[i] * dp_[i] * factorial_inv[size[i] - 1] * factorial_inv[size_[i] - 1]
    ans %= mod
    print(ans)
