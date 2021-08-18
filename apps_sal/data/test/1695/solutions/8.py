def mp():
    return map(int, input().split())


n, m = mp()
s = [input() for i in range(n)]
a = list(mp())

ans = 0
for j in range(m):
    cnt = [0] * 5
    for i in range(n):
        cnt[ord(s[i][j]) - 65] += 1
    ans += a[j] * max(cnt)

print(ans)
