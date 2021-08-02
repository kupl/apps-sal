from bisect import *

n = int(input())
l = sorted(list(map(int, input().split())))

cnt = 0

for i in range(n):
    a = l[i]
    for j in range(i + 1, n):
        b = l[j]
        k = bisect_left(l, a + b)
        cnt += k - (j + 1)
print(cnt)
