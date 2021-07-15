from math import gcd

N = int(input())
a = list(map(int, input().split()))

ans = a[0]
for i in range(1, N):
    ans = gcd(ans, a[i])
print(ans)

