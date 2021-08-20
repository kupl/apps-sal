import sys
input = sys.stdin.readline


def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b:
        (a, b) = (b, a % b)
    return a


(n, m, q) = list(map(int, input().split()))
g = gcd(n, m)
n = n // g
m = m // g
for _ in range(q):
    (sx, sy, ex, ey) = list(map(int, input().split()))
    a = (sy - 1) // (n if sx == 1 else m)
    b = (ey - 1) // (n if ex == 1 else m)
    print('YES' if a == b else 'NO')
