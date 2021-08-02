from bisect import bisect_left as bl, bisect_right as br
N, K = list(map(int, input().split()))
M = sorted([int(a) for a in input().split()])[::-1]
C = [0] + [int(a) for a in input().split()]
ANS = [{}]
S = [0]
for m in M:
    a = br(S, -C[m])
    if a >= len(ANS):
        ANS.append({})
        S.append(0)
    if m not in ANS[a]:
        ANS[a][m] = 1
    else:
        ANS[a][m] += 1
    S[a] -= 1

print(len(ANS))
for ans in ANS:
    L = []
    for a in ans:
        L += [a] * ans[a]
    print(len(L), *L)
