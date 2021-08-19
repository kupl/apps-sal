K = int(input())
S = input()
T = ''
if K >= len(S):
    print(S)
else:
    for i in range(K):
        T += S[i]
    print(T + '...')
