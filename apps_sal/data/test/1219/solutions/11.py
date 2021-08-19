N = int(input())
(a, b, c, d, e) = (float('-inf'), float('-inf'), float('-inf'), 0, 1)
for x in map(int, input().split()):
    (a, b, c, d, e) = (max(c + x, b - x), max(a + x, c - x), max(b + x, a - x, d - e * x), d + e * x, -e)
print([d, b][N > 1])
