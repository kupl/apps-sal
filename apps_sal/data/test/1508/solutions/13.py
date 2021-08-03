n = int(input())
a = list(map(int, input().split()))
a.sort()
s = a[0]
a = a[1:]
print(a[n - 2], *a[:n - 2], end=' ')
print(s)
