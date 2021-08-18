
import time

n = int(input())
b = [int(i) for i in input().split()]

start = time.time()

ans = b[0]
if ans < 0:
    ans = - ans

for i in range(1, n):
    d = b[i] - b[i - 1]
    if d < 0:
        d = - d
    ans += d

print(ans)
finish = time.time()
