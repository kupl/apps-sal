(n, c) = map(int, input().split())
cnt = [[0 for _ in range(10 ** 5 + 1)] for _ in range(c)]
for _ in range(n):
    (s, t, _c) = map(int, input().split())
    for j in range(s, t + 1):
        cnt[_c - 1][j] = 1
ans = 0
for i in range(10 ** 5 + 1):
    ans = max(ans, sum((cnt[j][i] for j in range(c))))
print(ans)
