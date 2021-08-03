from math import sqrt
R, D = map(int, input().split())
D = R - D
n = int(input())


cnt = 0
for i in range(n):
    x, y, r = map(int, input().split())

    p = x * x + y * y
    if (D + r)**2 <= p <= (R - r)**2:
        cnt += 1

print(cnt)
