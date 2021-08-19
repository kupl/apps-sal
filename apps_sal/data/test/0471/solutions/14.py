(n, p) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
if n == 1:
    print(0)
elif n == 2:
    print(min(abs(a[0] - p), abs(a[1] - p)))
else:
    a1 = min(abs(a[0] - p), abs(a[-2] - p)) + abs(a[0] - a[-2])
    a2 = min(abs(a[1] - p), abs(a[-1] - p)) + abs(a[1] - a[-1])
    print(min(a1, a2))
