A11, A12, A13 = list(map(int, input().split()))
A21, A22, A23 = list(map(int, input().split()))
A31, A32, A33 = list(map(int, input().split()))
A = [[A11, A12, A13], [A21, A22, A23], [A31, A32, A33]]

N = int(input())
b = [int(input()) for _ in range(N)]

for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            A[i][j] = 'YES'


if A[1][1] == 'YES':
    if A[1][0] == A[1][2] == 'YES' or A[0][1] == A[2][1] == 'YES' or A[0][0] == A[2][2] == 'YES' or A[0][2] == A[2][0] == 'YES':
        print('Yes')
    else:
        print('No')

else:
    if A[0][0] == A[0][1] == A[0][2] == 'YES' or A[0][0] == A[1][0] == A[2][0] == 'YES' or A[2][0] == A[2][1] == A[2][2] == 'YES' or A[0][2] == A[1][2] == A[2][2] == 'YES':
        print('Yes')

    else:
        print('No')
