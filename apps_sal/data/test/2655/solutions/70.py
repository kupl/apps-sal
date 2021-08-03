import math

n = int(input())
f = list(map(int, input().split()))
f.sort()
ans = 0

for i in range(1, n):
    ans += f[n - math.floor(i / 2) - 1]

print(ans)
