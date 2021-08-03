import math

n, d = map(int, input().split())

xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

count = 0

for i in range(n):
    if d >= math.sqrt(x[i]**2 + y[i]**2):
        count += 1
print(count)
