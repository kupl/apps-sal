A11, A12, A13 = map(int, input().split())
A21, A22, A23 = map(int, input().split())
A31, A32, A33 = map(int, input().split())
A = [[A11, A12, A13], [A21, A22, A23], [A31, A32, A33]]
N = int(input())
b = []
for x in range(N):
    b.append(int(input()))
    for i in range(3):
        for j in range(3):
            A[i][j] = 'YES' if b[x] == A[i][j] else A[i][j]
if A[0][0] == A[0][1] == A[0][2] == 'YES' or A[1][0] == A[1][1] == A[1][2] == 'YES' or A[2][0] == A[2][1] == A[2][2] == 'YES' or \
    A[0][0] == A[1][0] == A[2][0] == 'YES' or A[0][1] == A[1][1] == A[2][1] == 'YES' or A[0][2] == A[1][2] == A[2][2] == 'YES' or \
        A[0][0] == A[1][1] == A[2][2] == 'YES' or A[0][2] == A[1][1] == A[2][0] == 'YES':
    print('Yes')
else:
    print('No')
