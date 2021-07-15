K = int(input())
S = input()

S_len = len(S)

if len(S)<=K:
    print(S)
else:
    print(S[0:K]+'...')
