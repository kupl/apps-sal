n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.sort()
ans = n
c = 1
for i in range(0, n - 1):
    if a[i] == a[i + 1]:
        c += 1
    elif (a[i] + k >= a[i + 1]):
        ans -= c
        c = 1
    else:
        c = 1
print(ans)
