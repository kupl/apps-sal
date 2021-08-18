
import time

n = int(input())
a = [int(i) for i in input().split()]

start = time.time()

a = sorted(a)

now = 1

for i in range(n):
    if a[i] >= now:
        a[i] = now
        now = now + 1

print(now)
finish = time.time()
