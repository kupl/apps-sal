(l, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
if k >= 3:
    print(max(a))
elif k == 1:
    print(min(a))
elif a[0] > a[-1]:
    print(max(a[0], min(a[1:])))
else:
    print(max(a[-1], min(a[:-1])))
