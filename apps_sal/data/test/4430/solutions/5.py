(n, m, k) = [int(s) for s in input().split()]
a = [int(s) for s in input().split()]
ans = 0
boxi = 0
rem_size = k
for i in range(n - 1, -1, -1):
    if a[i] > k:
        break
    if a[i] > rem_size:
        if boxi >= m - 1:
            break
        else:
            boxi += 1
            rem_size = k
    rem_size -= a[i]
    ans += 1
print(ans)
