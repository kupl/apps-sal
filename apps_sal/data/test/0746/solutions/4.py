from math import sqrt
(a, b) = map(int, input().split())
n = int(input())
time = float('inf')
for i in range(n):
    (x, y, v) = map(int, input().split())
    time = min(time, sqrt((a - x) ** 2 + (b - y) ** 2) / v)
print(time)
