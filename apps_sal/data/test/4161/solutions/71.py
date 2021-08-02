from math import gcd

n = int(input())

ans = 0


for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            ans += gcd(gcd(i, j), k)

print(ans)
