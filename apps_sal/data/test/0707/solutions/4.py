n, m = map(int, input().split())
x = list(map(int, input().split()))
p = list(map(int, input().split()))
d = [x[i] - x[i - 1] for i in range(1, n)]


def gcd(a, b):
    if a == b:
        return a
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(a % b, b)


z = d[0]
for i in d:
    z = gcd(z, i)
a = []
f = False
for i in range(m):
    if z % p[i] == 0:
        print('YES')
        print(x[0], i + 1)
        f = True
        break
if not f:
    print('NO')
