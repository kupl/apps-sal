n, m = list(map(int, input().split()))
A = []

for i in range(n):
    A.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if A[i][j] == 1 and (i in [0, n - 1] or j in [0, m - 1]):
            print(2)
            return
print(4)

