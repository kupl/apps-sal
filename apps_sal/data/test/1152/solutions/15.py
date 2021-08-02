def Solve(A, B, n, m):
    for i in range(n - 1):
        for j in range(m - 1):
            if A[i][j] != B[i][j]:
                A[i][j] = int(not A[i][j])
                A[i][j + 1] = int(not A[i][j + 1])
                A[i + 1][j] = int(not A[i + 1][j])
                A[i + 1][j + 1] = int(not A[i + 1][j + 1])

    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                print('No')
                return
    print('Yes')


def main():
    n, m = list(map(int, input().split()))
    A = []
    B = []
    for i in range(n):
        A.append(list(map(int, input().split())))
    for i in range(n):
        B.append(list(map(int, input().split())))

    Solve(A, B, n, m)


main()
