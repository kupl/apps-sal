import math


def ria():
    return [int(i) for i in input().split()]


n = ria()[0]

ar = ria()
for i in range(0, n//2, 2):
    ar[i], ar[n - i - 1] = ar[n - i - 1], ar[i]

for i in ar:
    print(i,end=' ')
