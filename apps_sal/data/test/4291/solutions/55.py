N, Q = map(int, input().split())
S = " " + input()
l = []
r = []
for _ in range(Q):
    _l, _r = map(int, input().split())
    l.append(_l)
    r.append(_r)
dp = [0] * (N + 2)
cnt = 0
for i in range(1, N):
    if S[-i] == "C" and S[-i - 1] == "A":
        cnt += 1
    dp[N - i] = cnt
ans = 0
for q in range(Q):
    ans = dp[l[q]] - dp[r[q] + 1]
    if r[q] < N:
        if S[r[q]] == "A" and S[r[q] + 1] == "C":
            ans -= 1
    print(ans)
