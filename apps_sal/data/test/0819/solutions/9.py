(n, k) = list(map(int, input().split()))
a = [int(i) for i in input().split()]
if k == 1 or n == 1:
    print(min(a))
elif k >= 3:
    print(max(a))
else:
    print(max(a[0], a[-1]))
