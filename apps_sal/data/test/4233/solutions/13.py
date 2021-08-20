(N, M) = list(map(int, input().split()))
L = []
for a in range(N):
    L.append(list(input()))
ANS = []
for i in range(N):
    for j in range(M):
        if L[i][j] == '*' or L[i][j] == '-':
            k = 1
            l = min(i, j, N - 1 - i, M - 1 - j)
            while k <= l:
                if (L[i + k][j] == '*' or L[i + k][j] == '-') and (L[i][j + k] == '*' or L[i][j + k] == '-') and (L[i - k][j] == '*' or L[i - k][j] == '-') and (L[i][j - k] == '*' or L[i][j - k] == '-'):
                    L[i][j] = '-'
                    L[i + k][j] = '-'
                    L[i - k][j] = '-'
                    L[i][j + k] = '-'
                    L[i][j - k] = '-'
                    k += 1
                else:
                    break
            if k > 1:
                ANS.append((i + 1, j + 1, k - 1))
f = True
for a in L:
    if '*' in a:
        f = False
        break
if f:
    print(len(ANS))
    for a in ANS:
        print(' '.join(map(str, a)))
else:
    print(-1)
