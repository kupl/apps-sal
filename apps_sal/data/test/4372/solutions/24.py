n = int(input())
a = list(map(int, input().split()))
M = max(a)


def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


r = M - a[0]
for i in range(1, n):
    r = gcd(r, M - a[i])
ans = 0
for i in a:
    ans += (M - i) // r
print(ans, r)
