for t in range(int(input())):
    (n, p) = map(int, input().split())
    (i, j) = (1, 2)
    for k in range(2 * n + p):
        print(i, j)
        j += 1
        if j > n:
            i += 1
            j = i + 1
