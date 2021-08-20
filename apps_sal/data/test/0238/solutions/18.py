(n, m, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
sa = [0] * n
ans = 0
for i in range(n):
    sa[i] = a[i] - k
    s = a[i]
    for j in range(i - 1, max(-1, i - m - 1), -1):
        sa[i] = max(sa[i], sa[j] + s - k)
        s += a[j]
    if i < m:
        sa[i] = max(sa[i], s - k)
    sa[i] = max(sa[i], 0)
    ans = max(ans, sa[i])
print(ans)
