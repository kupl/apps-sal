n, m = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]


def rev(i, j):
    A[i][j] ^= 1
    A[i + 1][j] ^= 1
    A[i][j + 1] ^= 1
    A[i + 1][j + 1] ^= 1


for i in range(n - 1):
    for j in range(m - 1):
        # A[i][j] -> B[i][j]
        if A[i][j] != B[i][j]:
            rev(i, j)

if A == B:
    print('Yes')
else:
    print('No')
