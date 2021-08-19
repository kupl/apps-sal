(n, k) = list(map(int, input().split()))
s = '$' + input()
cnt = [[0] * (n + 1) for i in range(n + 1)]
cnt[0][0] = 1
for l in range(1, n + 1):
    for i in range(l, n + 1):
        used = [False] * 26
        for j in range(i, n + 1):
            x = ord(s[j]) - ord('a')
            if not used[x]:
                cnt[l][j] += cnt[l - 1][i - 1]
                used[x] = True
ans = 0
for l in range(n, -1, -1):
    s = sum(cnt[l])
    if s < k:
        ans += (n - l) * s
        k -= s
    else:
        ans += (n - l) * k
        k = 0
        break
if k > 0:
    ans = -1
print(ans)
