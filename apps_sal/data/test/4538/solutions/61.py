from math import sqrt
n, d = list(map(int, input().split()))
x_y = [[int(i) for i in input().split()] for i in range(n)]


cnt = 0
for x, y in x_y:
    route = sqrt(x ** 2 + y ** 2)
    if route <= d:
        cnt += 1

print(cnt)
