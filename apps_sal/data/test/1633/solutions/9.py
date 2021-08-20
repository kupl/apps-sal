(n, m, k) = map(int, input().split())
A = [[0] * (m + 1) for i in range(n + 1)]
counter = 0
flag = True
for i in range(k):
    counter += 1
    (i, j) = map(lambda x: int(x) - 1, input().split())
    A[i][j] = 1
    if A[i][j - 1] == 1 and A[i - 1][j - 1] == 1 and (A[i - 1][j] == 1):
        print(counter)
        flag = False
        break
    if A[i - 1][j] == 1 and A[i - 1][j + 1] == 1 and (A[i][j + 1] == 1):
        print(counter)
        flag = False
        break
    if A[i][j - 1] == 1 and A[i + 1][j - 1] == 1 and (A[i + 1][j] == 1):
        print(counter)
        flag = False
        break
    if A[i][j + 1] == 1 and A[i + 1][j] == 1 and (A[i + 1][j + 1] == 1):
        print(counter)
        flag = False
        break
if flag == True:
    print(0)
