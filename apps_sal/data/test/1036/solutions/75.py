N, K = list(map(int, input().split()))
S = input()
D = {'R': 0, 'P': 1, 'S': 2}


def winner(a, b):
    if (b - a) % 3 == 1:
        return b
    else:
        return a


L = [[0] * N for _ in range(K)]
A = [D[S[i]] for i in range(N)] * 2

for i in range(K):
    for j in range(N):
        L[i][j] = winner(A[2 * j], A[2 * j + 1])
    A = L[i] * 2
ans = L[-1][0]
if ans == 0:
    print('R')
elif ans == 1:
    print('P')
else:
    print('S')
