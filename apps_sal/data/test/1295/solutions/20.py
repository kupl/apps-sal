(n, m) = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
ans = -1
if m == 1:
    for i in x:
        if abs(i - y[0]) > ans:
            ans = abs(i - y[0])
else:
    c = 0
    p = 0
    q = 1
    while c != n:
        if y[p] <= x[c] and y[q] >= x[c]:
            ans = max(ans, min(y[q] - x[c], x[c] - y[p]))
            c += 1
        elif y[q] < x[c]:
            if q != m - 1:
                p += 1
                q += 1
            else:
                ans = max(ans, x[c] - y[q])
                c += 1
        elif y[p] > x[c]:
            ans = max(ans, y[p] - x[c])
            c += 1
print(ans)
