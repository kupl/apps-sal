def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


n = int(input())
a = [int(c) for c in input().split()]
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])
ans = 0
for i in range(1, int(g ** 0.5) + 1):
    if g % i == 0:
        if g // i != i:
            ans += 2
        else:
            ans += 1
print(ans)
