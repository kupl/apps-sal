K = int(input())
ans = 0


def gcd(x, y):
    if y == 0:
        return x
    if x >= y:
        return gcd(y, x % y)
    if x < y:
        return gcd(x, y % x)


for i in range(1, K + 1):
    ans += i
for i in range(1, K + 1):
    for j in range(i + 1, K + 1):
        ans += gcd(i, j) * 6
for i in range(1, K + 1):
    for j in range(i + 1, K + 1):
        for k in range(j + 1, K + 1):
            ans += gcd(gcd(i, j), k) * 6
print(ans)
