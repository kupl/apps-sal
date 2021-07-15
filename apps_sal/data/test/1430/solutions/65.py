N, K = [int(_) for _ in input().split()]
S = input()

S = "0" + S + "0"

X = []
for i in range(N+1):
    if S[i] == "0" and S[i+1] == "1":
        st = i+1
    if S[i] == "1" and S[i+1] == "0":
        en = i
        X.append((st, en))
M = len(X)

ans = 0
for i in range(len(X) - K):
    st = X[i][0]
    en = X[i+K][1]
    ans = max(ans, en - st + 1)

if M == 0 or M + 2 < K:
    ans = N

if K <= M:
    en = X[K-1][1]
    ans = max(ans, en - 1 + 1)
    st = X[-K][0]
    ans = max(ans, N - st + 1)

print(ans)

