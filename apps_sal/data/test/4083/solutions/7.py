n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = [[0, 0] for i in range(200001)]
a.sort()
for i in range(n):
    ans[a[i]][0] += 1
for i in range(n):
    s = a[i]
    d = 1
    while (s > 0):
        s = s // 2
        if ans[s][0] < k:
            ans[s][0] += 1
            ans[s][1] += d
        d += 1
mi = 100000000
for i in range(len(ans)):
    if ans[i][0] >= k:
        if ans[i][1] < mi:
            mi = ans[i][1]
print(mi)
