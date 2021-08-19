(a, b) = list(map(int, input().split()))
n = int(input())
minT = 1000000000.0
for _ in range(n):
    (x, y, v) = list(map(int, input().split()))
    d = ((a - x) ** 2 + (b - y) ** 2) ** 0.5
    t = d / v
    minT = min(minT, t)
print(minT)
