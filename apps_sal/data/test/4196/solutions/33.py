def gcd(x, y):
    if x == 0 or y == 0:
        return max(x, y)
    if x < y:
        x, y = y, x
    if x % y == 0:
        return y
    return gcd(y, x % y)


n = int(input())
a = list(map(int, input().split()))
L = [a[0]] * n
R = [a[-1]] * n
for i in range(n - 1):
    L[i + 1] = gcd(L[i], a[i + 1])
    R[-i - 2] = gcd(R[-i - 1], a[-i - 2])
ans = 1
L = [0] + L
R = R + [0]
for i in range(n):
    ans = max(ans, gcd(L[i], R[i + 1]))
print(ans)
