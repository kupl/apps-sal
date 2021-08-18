a, b, c = map(int, input().split())
if (1 <= a & a <= 100) & (1 <= b & b <= 100) & (1 <= c & c <= 100):
    d_ab = b - a
    d_bc = c - b
    if d_ab == d_bc:
        print('YES')
    else:
        print('NO')
