import bisect
n = int(input())
a = list(map(int, input().split()))
a.sort()
num = a[-1] / 2
b = bisect.bisect_left(a, num)
if abs(num - a[b]) < abs(num - a[b - 1]):
    print(a[-1], a[b])
else:
    print(a[-1], a[b - 1])
