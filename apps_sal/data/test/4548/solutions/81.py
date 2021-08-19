(n, m, x) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(m):
    if a[i] > x:
        if i < m - i:
            ans = i
        else:
            ans = m - i
        break
print(ans)
