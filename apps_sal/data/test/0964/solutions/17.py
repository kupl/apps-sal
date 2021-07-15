x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))

def solve(x1, y1, x2, y2, x3, y3):
    n = max(x1, y1, x2, y2, x3, y3)
    sum_area = x1 * y1 + x2 * y2 + x3 * y3
    if sum_area != n * n:
        return -1, None
    if x1 < y1:
        x1, y1 = y1, x1
    if x2 < y2:
        x2, y2 = y2, x2
    if x3 < y3:
        x3, y3 = y3, x3
    if x1 == x2 == x3:
        bil = ['A' * n for i in range(y1)]
        bil.extend(['B' * n for i in range(y2)])
        bil.extend(['C' * n for i in range(y3)])
        return n, bil
    xys = [(x1, y1, 'A'), (x2, y2, 'B'), (x3, y3, 'C')]
    xys.sort(reverse = True)
    x1, y1, C1 = xys[0]
    x2, y2, C2 = xys[1]
    x3, y3, C3 = xys[2]
    if x2 == x1:
        return -1, None
    m = n - y1
    if (x2 == m or y2 == m) and (x3 == m or y3 == m):
        bil = [C1 * n for i in range(y1)]
        w2 = x2 + y2 - m
        w3 = x3 + y3 - m
        bil.extend([C2 * w2 + C3 * w3 for i in range(m)])
        return n, bil
    return -1, None

n, pattern = solve(x1, y1, x2, y2, x3, y3)
if n == -1:
    print(-1)
else:
    print(n)
    for row in pattern:
        print(row)

