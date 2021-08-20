(n, m) = map(int, input().split())
a = [[] for i in range(m)]
for _ in range(n):
    (t, s) = map(int, input().split())
    a[t - 1].append(s)
pre = [0] * n
for i in range(m):
    a[i].sort(reverse=True)
    sum = 0
    k = len(a[i])
    for j in range(k):
        sum = sum + a[i][j]
        if sum < 0:
            break
        pre[j] = pre[j] + sum
print(max(max(pre), 0))
