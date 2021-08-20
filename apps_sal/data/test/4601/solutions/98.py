(n, k) = [int(i) for i in input().split()]
a = sorted([int(i) for i in input().split()])
if k <= 0:
    print(sum(a))
else:
    print(sum(a[:-k]))
