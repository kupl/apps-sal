(N, S) = input().split()
N = int(N)
cnt_AT = [0] * (N + 1)
cnt_CG = [0] * (N + 1)
for n in range(N):
    if S[n] == 'A':
        cnt_AT[n + 1] = cnt_AT[n] + 1
        cnt_CG[n + 1] = cnt_CG[n]
    if S[n] == 'T':
        cnt_AT[n + 1] = cnt_AT[n] - 1
        cnt_CG[n + 1] = cnt_CG[n]
    if S[n] == 'C':
        cnt_AT[n + 1] = cnt_AT[n]
        cnt_CG[n + 1] = cnt_CG[n] + 1
    if S[n] == 'G':
        cnt_AT[n + 1] = cnt_AT[n]
        cnt_CG[n + 1] = cnt_CG[n] - 1
ans = 0
for i in range(N - 1):
    for j in range(i + 2, N + 1, 2):
        at = cnt_AT[j] - cnt_AT[i]
        cg = cnt_CG[j] - cnt_CG[i]
        if at == 0 and cg == 0:
            ans += 1
print(ans)
