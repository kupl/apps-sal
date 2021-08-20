import bisect
n = int(input())
a = sorted(list(map(int, input().split())))
x = a[-1]
N = a[-1] // 2
a = a[:-1]
y = bisect.bisect_left(a, N)
if len(a) <= y:
    ans = a[y - 1]
else:
    ans = a[y]
    if 0 < y and abs(N - ans) > abs(N - a[y - 1]):
        ans = a[y - 1]
    if y < len(a) - 1 and abs(N - ans) > abs(N - a[y + 1]):
        ans = a[y + 1]
print(x, ans)
