n = int(input())
a = [int(s) for s in input().split()]
a.sort()
mn1 = a[n - 2] - a[0]
mn2 = a[n - 1] - a[1]
print(min(mn1, mn2))
