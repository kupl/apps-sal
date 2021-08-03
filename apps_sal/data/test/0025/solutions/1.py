n, k = [int(x) for x in input().split()]

if k > n * n:
    print('-1')
else:

    res = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i > j:
                res[i][j] = res[j][i]
            elif i == j:
                if k > 0:
                    res[i][j] = 1
                    k -= 1
            else:
                if k > 1:
                    res[i][j] = 1
                    k -= 2
    for i in range(n):
        print(' '.join(str(res[i][j]) for j in range(n)))
