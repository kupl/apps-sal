K = int(input())

ans = 0

def gcd(x, y):
    if x == 1 or y == 1:
        return 1
    else:
        while True:
            if x >= y:
                x %= y
            else:
                y %= x
            if x == 0 or y == 0:
                break
        return x + y

for i in range(1, K + 1):
    for j in range(i, K + 1):
        for k in range(j, K + 1):
            if i == j == k:
                ans += gcd(i, gcd(j, k))
            elif i == j or j == k or k == i:
                ans += gcd(i, gcd(j, k)) * 3
            else:
                ans += gcd(i, gcd(j, k)) * 6

print(ans)
