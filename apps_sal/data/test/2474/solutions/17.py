import sys
INF = 1000000000.0
mod = 1000000000.0 + 7
n = int(input())
lit = list(map(int, input().split()))
lit.sort()
ans = 0
for i in range(n):
    ans = (ans + lit[i] * (n - i + 1) % mod) % mod
for i in range(n - 1):
    ans = ans * 4 % mod
ans = int(ans)
print(ans)
