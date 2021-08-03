import bisect
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = input()
Next = [[float("inf")] * (26) for _ in range(n + 1)]
for i in reversed(range(n)):
    for j in range(26):
        Next[i][j] = Next[i + 1][j]
    Next[i][ord(s[i]) - 97] = i
DP = [[0] * (n + 1) for _ in range(n + 1)]
DP[0][0] = 1
for i in range(n):
    for j in range(26):
        nxt = Next[i][j]
        for l in range(n):
            if nxt < float("inf"):
                DP[nxt + 1][l + 1] += DP[i][l]
Ans = [0] * (n + 1)
for i in range(n + 1):
    for j in range(n + 1):
        Ans[n - j] += DP[i][j]
Ans2 = [0]
for i in range(n + 1):
    Ans2.append(Ans2[-1] + Ans[i])
if Ans2[-1] < k:
    print(-1)
else:
    ind = bisect.bisect_left(Ans2, k)
    ans, num = 0, 0
    for i in range(ind - 1):
        ans += i * Ans[i]
        num += Ans[i]
    ans += (ind - 1) * (k - num)
    print(ans)
