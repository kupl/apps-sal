(n, m) = [int(x) for x in input().split()]
arr = [[int(x) for x in input().split()] for i in range(n)]
val = [[1] * m for i in range(n)]
for i in range(m):
    for j in range(n - 2, -1, -1):
        if arr[j][i] <= arr[j + 1][i]:
            val[j][i] = val[j + 1][i] + 1
best = [max(i) for i in val]
ans = ''
t = int(input())
for i in range(t):
    (c, d) = [int(x) for x in input().split()]
    if best[c - 1] >= d - c + 1:
        ans += 'Yes\n'
    else:
        ans += 'No\n'
print(ans)
