def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def norm(a, b, c):
    k = gcd(gcd(a, b), c)
    return (a // k, b // k, c // k)


def line(A, B):
    a = A[1] - B[1]
    b = B[0] - A[0]
    c = -a * A[0] - b * A[1]
    return norm(a, b, c)


def dist_line(A, l):
    (x, y) = A
    (a, b, c) = l
    d = a * a + b * b
    res = a * x + b * y + c
    return res


def read():
    return list(map(int, input().split()))


(n, w, v, u) = read()
p = [tuple(read()) for i in range(n)]
l = line((0, 0), (v, u))
mind = float('inf')
maxd = -float('inf')
d = 0
for P in p:
    curd = dist_line(P, l)
    maxd = max(maxd, curd)
    mind = min(mind, curd)
    if mind == curd:
        x = (-l[1] * P[1] - l[2]) / l[0]
        d = P[0] - x
ans = w / u
if mind * maxd < 0:
    ans += d / v
print(ans)
