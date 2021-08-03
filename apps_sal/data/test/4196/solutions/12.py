import math

n = int(input())
a = list(map(int, input().split()))
L = [0] * (n + 1)
R = [0] * (n + 1)
for i in range(n):
    L[i + 1] = math.gcd(L[i], a[i])
    R[-2 - i] = math.gcd(R[-1 - i], a[-1 - i])

ans = 0
for i in range(n):
    G = math.gcd(L[i], R[i + 1])
    ans = max(ans, G)
print(ans)
