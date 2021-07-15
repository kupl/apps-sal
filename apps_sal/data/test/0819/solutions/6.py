n, k = map(int, input().split())
a = list(map(int, input().split()))
if k == 1:
    print(min(a))
elif k >= 3:
    print(max(a))
else:
    print(max(a[0], a[-1]))
