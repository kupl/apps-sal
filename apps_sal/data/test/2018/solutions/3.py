def solve(x1, y1, x2, y2):
    if x1 == x2:
        if x1 == 1:
            return (y1 - 1) // n1 == (y2 - 1) // n1
        else:
            return (y1 - 1) // m1 == (y2 - 1) // m1
    else:
        if x1 == 1:
            return (y1 - 1) // n1 == (y2 - 1) // m1
        else:
            return (y1 - 1) // m1 == (y2 - 1) // n1

gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
n, m, q = map(int, input().split())
k = gcd(n, m)
n1 = n // k
m1 = m // k
res = []
for i in range(q):
    sx, sy, ex, ey = map(int, input().split())
    res.append("YES" if solve(sx, sy, ex, ey) else "NO")
print('\n'.join(res))
