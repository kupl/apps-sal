n, m = list(map(int, input().split()))

A = []
B = []

for i in range(n):
    A.append(list(map(int, input().split())))

for i in range(n):
    B.append(list(map(int, input().split())))
    
v = True

for r in range(n-1):
    for c in range(m - 1):
        if A[r][c] != B[r][c]:
            A[r][c] ^= 1
            A[r+1][c] ^= 1
            A[r][c+1] ^= 1
            A[r+1][c+1] ^= 1
    if A[r][m-1] != B[r][m-1] : v = False
if A[n-1] != B[n-1]: v = False

if v == True:
    print("Yes")
else:
    print("No")

