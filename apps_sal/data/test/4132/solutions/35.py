import math

n = int(input())
a = list(map(int, input().split()))

ans = 10**10
for i in range(1, n):
    ans = min(ans, math.gcd(a[0], a[i]))
print(ans)
