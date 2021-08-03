n = int(input())
a = []
for i in range(n):
    l, r = list(map(int, input().split()))
    a.append([l, 1])
    a.append([r + 1, -1])
a.sort()

c = 0
ans = [0] * (n + 1)
for i in range(2 * n):
    c += a[i][1]
    if (i + 1) < len(a) and a[i][0] != a[i + 1][0]:
        ans[c] += a[i + 1][0] - a[i][0]

print(*ans[1:])
