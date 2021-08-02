n, d = map(int, input().split())
a = [int(x) for x in input().split()]
a.sort()
l = 0
r = n - 1
mn = n
for i in range(n):
    l = i
    r = n
    c = a[i] + d
    while r - l > 1:
        mid = (r + l) // 2
        if a[mid] > c:
            r = mid
        else:
            l = mid
    mn = min(mn, n - (l - i + 1))
print(mn)
