import math
N = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(1, N):
    ans = ans * a[i] // math.gcd(ans, a[i])
tmp = ans - 1
mod = 0
f = 0
for i in range(N):
    mod = tmp % a[i]
    f += mod
print(f)
