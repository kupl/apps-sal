(n, k) = map(int, input().split())
cnt = [[0 for i in range(0, 3)] for j in range(0, n)]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(0, n):
    cnt[i][0] = b[i] - a[i]
    cnt[i][1] = a[i]
    cnt[i][2] = b[i]
cnt.sort()
ans = 0
for i in range(n - 1, n - k - 1, -1):
    ans += cnt[i][1]
for i in range(n - k - 1, -1, -1):
    ans += min(cnt[i][1], cnt[i][2])
print(ans)
