n = int(input())
a = []
for i in range(n):
    l, r = map(int, input().split())
    a.append([l, 1])
    a.append([r + 1, -1])
a.sort()
ans = [0] * (n + 1)
idx = 0
for i in range(len(a) - 1):
    idx += a[i][1]
    ans[idx] += a[i + 1][0] - a[i][0]
for i in range(1, n + 1):
    print(ans[i], end=" ")
print()
