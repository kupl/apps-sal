n = int(input())
a1, b1, a2, b2 = map(int, input().split())
s = (a2 - a1) * (b2 - b1)
for i in range(n - 1):
    x1, y1, x2, y2 = map(int, input().split())
    a1, b1, a2, b2 = min(a1, x1), min(b1, y1), max(a2, x2), max(b2, y2)
    s += (x2 - x1) * (y2 - y1)
print('YES' if a2 - a1 == b2 - b1 and s == (a2 - a1) * (b2 - b1) else 'NO')
