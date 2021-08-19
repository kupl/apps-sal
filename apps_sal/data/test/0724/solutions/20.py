(n, d) = map(int, input().split())
a = [int(i) for i in input().split()]
a.sort()
ans = [[1000000000] * n for i in range(n)]
for l in range(n):
    for r in range(l, n):
        if max(a[l:r + 1]) - min(a[l:r + 1]) <= d:
            ans[l][r] = l + (n - r - 1)
print(min([min(i) for i in ans]))
