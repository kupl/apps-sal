N = int(input())
S = list(input())
W = [0] * N
E = [0] * N
W_pre = E_pre = 0
for i in range(N):
    if S[i] == 'W':
        W[i] = W_pre + 1
        E[i] = E_pre
    else:
        W[i] = W_pre
        E[i] = E_pre + 1
    W_pre = W[i]
    E_pre = E[i]
ans = N
for i in range(N):
    if i > 0:
        res1 = W[i - 1]
    else:
        res1 = 0
    res2 = E[N - 1] - E[i]
    ans = min(ans, res1 + res2)
print(ans)
