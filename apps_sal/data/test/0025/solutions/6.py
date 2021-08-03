
n, k = list(map(int, input().split()))

if k > n * n:
    print(-1)
else:
    b = [[0] * n for i in range(n)]
    c = 0
    i = 0
    j = 0
    t = -1
    while c < k:
        if i == j:
            b[i][j] = 1
            c += 1
            j += 1
            t = 0

        elif j == n:
            i += 1
            j = i
            t = 1

        else:

            b[i][j] = 1
            b[j][i] = 1
            j += 1
            c += 2
            t = 2

    if c == k:
        p = ""
        for q in range(n):
            for w in range(n):
                p += str(b[q][w]) + " "
            print(p)
            p = ""

    else:
        if t == 0:
            j -= 1
        if t == 1:
            i -= 1
            j = n - 1
        if t == 2:
            j -= 1
        b[i][j] = 0
        b[j][i] = 0
        b[i + 1][i + 1] = 1
        p = ""
        for q in range(n):
            for w in range(n):
                p += str(b[q][w]) + " "
            print(p)
            p = ""
