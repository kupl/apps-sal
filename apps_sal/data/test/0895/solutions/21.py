from bisect import bisect
n = int(input())
lst = list(map(int, input().split()))
t = int(input())
lst.sort()
res = 0
for (i, x) in enumerate(lst):
    j = bisect(lst, x + t)
    res = max(res, j - i)
print(res)
