import sys
input = sys.stdin.readline


def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)


n, m, q = map(int, input().split())
g = gcd(n, m)
n_wall = n // g; m_wall = m // g
for _ in range(q):
    a, b, c, d = map(int, input().split())
    if a == 1:
        r1 = (b + n_wall - 1) // n_wall
    else:
        r1 = (b + m_wall - 1) // m_wall
    if c == 1:
        r2 = (d + n_wall - 1) // n_wall
    else:
        r2 = (d + m_wall - 1) // m_wall
    print('YES' if r1 == r2 else 'NO')
