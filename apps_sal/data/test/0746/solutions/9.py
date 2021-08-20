def dist(a, b, x, y):
    return ((a - x) ** 2 + (b - y) ** 2) ** 0.5


(a, b) = list(map(int, input().split()))
n = int(input())
m = None
for i in range(n):
    (x, y, v) = list(map(int, input().split()))
    t = dist(a, b, x, y) / v
    if m is None or t < m:
        m = t
print(m)
