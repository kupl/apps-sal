(n, k) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
if k == 1:
    print(min(a))
elif k > 2:
    print(max(a))
else:
    print(max(a[0], a[-1]))
