from collections import Counter
n = int(input())
points = [[int(i) for i in input().split()] for _ in range(4 * n + 1)]
c_x = Counter(map(lambda a: a[0], points))
c_y = Counter(map(lambda a: a[1], points))
x = [a for a in c_x if c_x[a] >= n]
y = [a for a in c_y if c_y[a] >= n]
s_x = (min(x), max(x))
s_y = (min(y), max(y))
for p in points:
    if not (p[0] in s_x and s_y[0] <= p[1] <= s_y[1] or (p[1] in s_y and s_x[0] <= p[0] <= s_x[1])):
        print(*p)
