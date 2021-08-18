
import time
import math

n = int(input())
a = [int(i) for i in input().split()]

start = time.time()


min = math.ceil(a[0] / n)
mini = 0
for i in range(n):
    a[i] = math.ceil((a[i] - i) / n)
    if min > a[i]:
        mini = i
        min = a[i]

print(mini + 1)
finish = time.time()
