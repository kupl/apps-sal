_S = list(input())
T = list(input())

N = len(_S)
M = len(T)

candidates = []

for i in range(N - M + 1):
    if _S[i] == '?' or _S[i] == T[0]:
        S = _S.copy()
        flg = True
        for j in range(M):
            if S[i + j] == '?':
                S[i + j] = T[j]
            elif S[i + j] != T[j]:
                flg = False
                break
        if flg:
            for k in range(N):
                if S[k] == '?':
                    S[k] = 'a'
            candidates.append(''.join(S))

if len(candidates) == 0:
    print('UNRESTORABLE')
else:
    print((min(candidates)))
