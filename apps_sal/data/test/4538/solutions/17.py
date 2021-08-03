import math
n, d = map(int, input().split())
cnt = 0
for i in range(n):
    x, y = map(int, input().split())
    if d >= math.sqrt(x**2 + y**2):
        cnt += 1
    else:
        pass

print(cnt)
