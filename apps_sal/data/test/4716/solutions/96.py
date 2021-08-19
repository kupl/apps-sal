(n, k) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()
print(sum(a[n - k:n]))
