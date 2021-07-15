S = list(input())
N = len(S)

K = N // 2

if N % 2 == 0:
    if S[K - 1] == S[K]:
        tmp = S[K - 1]
    else:
        print (K)
        return
    i = 0
    while i < K and S[K - 1 - i] == S[K + i] == tmp:
        i += 1
    print (K + i)
else:
    tmp = S[K]
    i = 1
    while i <= K and S[K - i] == S[K + i] == tmp:
        i += 1
    print (K + i)
