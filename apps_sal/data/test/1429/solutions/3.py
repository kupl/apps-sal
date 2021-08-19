import itertools
(N, S) = input().split()
N = int(N)
AT = [0] * N
CG = [0] * N
for i in range(N):
    if S[i] == 'A':
        AT[i] = 1
    if S[i] == 'T':
        AT[i] = -1
    if S[i] == 'C':
        CG[i] = 1
    if S[i] == 'G':
        CG[i] = -1
AT = [0] + AT
CG = [0] + CG
ATC = list(itertools.accumulate(AT))
CGC = list(itertools.accumulate(CG))
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if ATC[i] == ATC[j + 1] and CGC[i] == CGC[j + 1]:
            ans += 1
print(ans)
