(n, m, k) = map(int, input().split())
a = [int(i) for i in input().split()]
cur = 0
ans = 0
box = k
i = n - 1
while i >= 0:
    obj = a[i]
    if obj <= box:
        box -= obj
        ans += 1
    else:
        cur += 1
        box = k
        if cur >= m:
            break
        continue
    i -= 1
print(ans)
