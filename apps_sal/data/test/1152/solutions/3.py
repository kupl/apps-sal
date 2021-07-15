n,m = list(map(int,input().split()))
A = [[int(x) for x in input().split()] for _ in range(n)]
B = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n-1):
    for j in range(m-1):
        if A[i][j] != B[i][j]:
            A[i][j] = 1 - A[i][j]
            A[i+1][j] = 1 - A[i+1][j]
            A[i][j+1] = 1 - A[i][j+1]
            A[i+1][j+1] = 1 - A[i+1][j+1]

if A == B:
    print('Yes')
else:
    print('No')

