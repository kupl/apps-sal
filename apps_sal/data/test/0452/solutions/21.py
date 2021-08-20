def gcd(x, y):
    while x > 0 and y > 0:
        if x > y:
            x %= y
        else:
            y %= x
    return x + y


(p, q) = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
p1 = 1
q1 = a[n - 1]
for i in range(n - 2, -1, -1):
    p1 += a[i] * q1
    z = p1
    p1 = q1
    q1 = z
z = p1
p1 = q1
q1 = z
g = gcd(p, q)
if g != 0:
    p /= g
    q /= g
g = gcd(p1, q1)
if g != 0:
    p1 /= g
    q1 /= g
if p == p1 and q == q1:
    print('YES')
else:
    print('NO')
