n = int(input())
l = list(map(int, input().split()))
maxl = max(l) + 1
dp = []
for i in range(maxl):
    dp.append([-1, -1])
for i in range(n):
    dp[l[i]][1] = i
for i in range(n - 1, -1, -1):
    dp[l[i]][0] = i
ll = []
lr = []
for i in range(n):
    ll.append(0)
    lr.append(0)
cnt = 0
for i in range(maxl):
    if dp[i][0] != -1:
        ll[dp[i][0]] = 1
        lr[dp[i][1]] = 1
        cnt += 1
ans = 0
for i in range(n):
    if lr[i] == 1:
        cnt -= 1
    if ll[i] == 1:
        ans += cnt
print(ans)
