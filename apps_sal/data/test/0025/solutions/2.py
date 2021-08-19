def main():
    (n, k) = map(int, input().split())
    if k > n ** 2:
        print(-1)
        return
    A = [[0] * n for _ in range(n)]
    i = 0
    j = 0
    while k > 1:
        A[i][j] = 1
        k -= 1
        j += 1
        while k > 1 and j < n:
            A[i][j] = 1
            A[j][i] = 1
            j += 1
            k -= 2
        i += 1
        j = i
    if k == 1:
        A[i][j] = 1
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=' ')
        print()


def __starting_point():
    main()


__starting_point()
