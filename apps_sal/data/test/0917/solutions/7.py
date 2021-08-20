(n, h, m) = list(map(int, input().split()))
ans = [h] * n
for i in range(m):
    (l, r, x) = list(map(int, input().split()))
    for j in range(l - 1, r):
        ans[j] = min(ans[j], x)
cnt = 0
for i in range(n):
    cnt += ans[i] * ans[i]
print(cnt)
