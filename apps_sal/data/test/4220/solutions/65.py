K = int(input())
S = str(input())
SS = str()
i = 0
if len(S) > K:
    for i in range(K):
        SS += S[i]
        i += 1
    print(SS + '...')
else:
    print(S)
