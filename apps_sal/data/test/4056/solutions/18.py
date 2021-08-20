def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
ln = [int(i) for i in input().split(' ')]
m = ln[0]
for i in range(1, len(ln)):
    m = gcd(m, ln[i])
d = 0
for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0:
        d += 2
        if i == m ** 0.5:
            d -= 1
print(d)
