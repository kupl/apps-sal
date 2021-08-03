n = int(input())
degree = n * [0]
for i in range(0, n - 1):
    u, v = input().split()
    u = int(u)
    v = int(v)
    u -= 1
    v -= 1
    degree[u] += 1
    degree[v] += 1
numL = 0
for i in range(0, n):
    if degree[i] == 1:
        numL += 1
mod = 1000000007
ans = (n - numL) * 2**(n - numL) + numL * 2**(n + 1 - numL)
print(ans % mod)
