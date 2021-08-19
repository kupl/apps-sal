from operator import itemgetter
(n, ma, mb) = list(map(int, input().split()))
abc = []
for i in range(n):
    abc.append([int(j) for j in input().split()])
abc.sort(key=itemgetter(2))
dp = [[10 ** 18 for i in range(401)] for j in range(401)]
dp[0][0] = 0
(p, q) = (0, 0)
for (a, b, c) in abc:
    for j in reversed(list(range(q + 1))):
        for i in range(p + 1):
            if dp[i][j] == 10 ** 18:
                continue
            else:
                dp[i + a][j + b] = min(dp[i + a][j + b], dp[i][j] + c)
    p += a
    q += b
ans = 1145141919
i = 1
while ma * i < 401 and mb * i < 401:
    ans = min(ans, dp[ma * i][mb * i])
    i += 1
if ans == 1145141919:
    print(-1)
else:
    print(ans)
