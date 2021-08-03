from math import sqrt

x, y = map(int, input().split())
n = int(input())
t = 10**9
for i in range(n):
    j, k, v = map(int, input().split())
    d = sqrt((x - j)**2 + (y - k)**2) / v
    t = min(t, d)
print(t)
