for _ in range(int(input())):
    n, k = map(int, input().split())
    mat = [[0] * n for _ in range(n)]
    for i in range(n):
        b = False
        for j in range(n):
            if i * n + j == k:
                b = True
                break
            mat[(i + j) % n][j] = 1
        if b:
            break
    if k % n == 0:
        print(0)
    else:
        print(2)
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end="")
        print()
