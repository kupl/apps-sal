N, M = map(int, input().split())
P = []
S = []
AC = [0] * (N + 1)
WA = [0] * (N + 1)
ac = 0
wa = 0
for i in range(M):
    p, s = input().split()
    P.append(int(p))
    S.append(s)
for i in range(M):
    if(S[i] == "WA" and AC[P[i]] == 0):
        WA[P[i]] += 1
    if(S[i] == "AC"):
        AC[P[i]] += 1
for i in range(1, N + 1):
    if(AC[i] >= 1):
        ac += 1
        wa += WA[i]
print(ac, wa)
