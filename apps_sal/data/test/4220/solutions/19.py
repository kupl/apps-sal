K = int(input())
S = str(input())

SK = S[0: (K)]

if len(S) <= K:
    print(S)
else:
    print(SK + '...')
