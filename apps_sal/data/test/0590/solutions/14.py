n, ans, j = int(input()), 0, 1
a = [int(i) for i in input().split()]
res, c, lft = [0] * n, [0] * (n + 1), [0] * (n + 1)
for i in a:
    c[i] += 1
while j <= n and c[j]:
    j += 1
for i in range(len(a)):
    if c[a[i]] > 1:
        if lft[a[i]] or a[i] > j:
            ans += 1
            c[a[i]] -= 1
            res[i] = j
            j += 1
            while j <= n and c[j]:
                j += 1
        else:
            lft[a[i]] = 1
            res[i] = a[i]
    else:
        res[i] = a[i]
print(ans)
print(*res)
    

