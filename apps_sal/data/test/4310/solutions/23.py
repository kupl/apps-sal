a = [int(x) for x in input().split()]
a1 = abs(a[1] - a[0]) + abs(a[1] - a[2])
a2 = abs(a[2] - a[0]) + abs(a[2] - a[1])
a3 = abs(a[2] - a[0]) + abs(a[1] - a[0])
print(min(a1,a2,a3))
