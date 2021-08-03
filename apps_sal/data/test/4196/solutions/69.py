import math

n = int(input())

a = list(map(int, input().split()))

L = [0]

for i in range(n):
    L.append(math.gcd(L[i], a[i]))

R = [0]
for i in range(n):
    R.append(math.gcd(R[i], a[n - 1 - i]))

ans = 1
for i in range(n):
    ans = max(ans, math.gcd(L[i], R[n - 1 - i]))

print(ans)
