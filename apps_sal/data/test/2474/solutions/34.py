import sys
INF = 1000000000.0
mod = 1000000000.0 + 7
n = int(input())
lit = list(map(int, input().split()))
lit.sort()
ans = 0
for i in range(n):
    ans = (ans + lit[i] * (n - i + 1) % mod) % mod
for i in range(2 * (n - 1)):
    ans = ans * 2 % mod
ans = int(ans)
print(ans)
