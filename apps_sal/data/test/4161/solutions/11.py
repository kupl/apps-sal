from math import gcd

k = int(input())


ans = 0
for x in range(1, k + 1):
    for y in range(1, k + 1):
        for z in range(1, k + 1):
            ans += gcd(gcd(x, y), z)

print(ans)
