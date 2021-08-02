import math
n, x = map(int, input().split())
L = list(map(int, input().split()))
L.append(x)
L.sort()
D = []
for i in range(n):
    d = L[i + 1] - L[i]
    D.append(d)

ans = D[0]
for i in range(1, n):
    ans = math.gcd(ans, D[i])

print(ans)
