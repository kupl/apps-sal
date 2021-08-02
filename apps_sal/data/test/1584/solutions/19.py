from bisect import *
n = int(input())
l = sorted(list(map(int, input().split())))
res = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        a, b = l[i], l[j]
        c_cnt = bisect_left(l, a + b) - j - 1
        res += c_cnt
print(res)
