N, M = map(int, input().split())
A, B = [''] * N, [''] * M
for i in range(N):
    A[i] = input()
for i in range(M):
    B[i] = input()

def check(x, y):
    if x + M > N or y + M > N: return False
    for i in range(M):
        for j in range(M):
            if A[x + i][y + j] != B[i][j]: return False
    return True

for i in range(N):
    for j in range(N):
        if check(i, j):
            print('Yes')
            return
print('No')
