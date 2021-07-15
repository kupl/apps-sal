def isIncreasing(matrix, n, m):
    for j in range(m-1):
        if matrix[0][j+1]<=matrix[0][j]: return False
    for i in range(n-1):
        if matrix[i+1][0]<=matrix[i][0]: return False
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j]<=matrix[i-1][j] or matrix[i][j]<=matrix[i][j-1]:
                return False
    return True

n, m = list(map(int, input().split()))
A = []
B = []
for i in range(n):
    A.append(list(map(int, input().split())))
for i in range(n):
    B.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        A[i][j], B[i][j] = min(A[i][j], B[i][j]), max(A[i][j], B[i][j])
if isIncreasing(A, n, m) and isIncreasing(B, n, m): print("Possible")
else: print("Impossible")

