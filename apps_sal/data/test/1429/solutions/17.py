(N, S) = input().split()
N = int(N)
AT = [0] * (N + 1)
CG = [0] * (N + 1)
for n in range(N):
    if S[n] == 'A':
        AT[n + 1] = 1
    if S[n] == 'T':
        AT[n + 1] = -1
    if S[n] == 'C':
        CG[n + 1] = 1
    if S[n] == 'G':
        CG[n + 1] = -1
for n in range(1, N + 1):
    AT[n] += AT[n - 1]
    CG[n] += CG[n - 1]
ans = 0
for i in range(N):
    for j in range(i + 2, N + 1, 2):
        at = AT[j] - AT[i]
        cg = CG[j] - CG[i]
        if at == 0 and cg == 0:
            ans += 1
print(ans)
