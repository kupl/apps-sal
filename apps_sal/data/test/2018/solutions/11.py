import math

n, m, q = list(map(int, input().split()))
g = math.gcd(n, m)
nm1 = [1, 1, 1]
nm1[1] = n // g
nm1[2] = m // g


def bsn(x, y):
    return (y - 1) // nm1[x]


for _ in range(q):
    sx, sy, ex, ey = list(map(int, input().split()))
    print("YES" if bsn(sx, sy) == bsn(ex, ey) else "NO")
