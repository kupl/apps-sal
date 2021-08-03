n = int(input())
a = list(map(int, input().split()))
maxi = -1
for i in range(n - 1, -1, -1):
    t = a[i]
    if a[i] > maxi:
        a[i] = 0
    else:
        a[i] = maxi - a[i] + 1
    maxi = max(maxi, t)
print(*a)
