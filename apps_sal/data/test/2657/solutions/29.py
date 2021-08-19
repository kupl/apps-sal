from bisect import bisect_left, bisect_right
n = int(input())
a = [int(x) for x in input().split()]
a.sort()
n = a[-1]
mid = a[-1] // 2
i = bisect_left(a[:-1], mid)
if i >= len(a) - 1:
    r = a[i - 1]
elif i == 0 or a[i] == mid:
    r = a[i]
elif a[i] - mid <= mid - a[i - 1]:
    r = a[i]
else:
    r = a[i - 1]
print(n, r)
