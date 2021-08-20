t = int(input())
d = []
for i in range(31):
    dd = []
    for j in range(31):
        dd.append([0] * 51)
    d.append(dd)
d[1][1][1] = 0
for i in range(1, 31):
    for j in range(1, 31):
        for k in range(1, min(i * j, 50) + 1):
            if k > i * j // 2:
                d[i][j][k] = d[i][j][i * j - k]
            elif i > j:
                d[i][j][k] = d[j][i][k]
            elif (i, j) != (1, 1):
                k = min(k, i * j - k)
                kk = i * j - k
                jj = i ** 2 * j * j ** 2 * i
                for l in range(1, i):
                    if k <= l * j:
                        jj = min(jj, d[l][j][k] + j ** 2)
                    else:
                        k1 = k - l * j
                        jj = min(jj, d[i - l][j][k1] + j ** 2)
                    if kk <= l * j:
                        if kk <= 50:
                            jj = min(jj, d[l][j][kk] + j ** 2)
                    else:
                        kk1 = kk - l * j
                        if kk1 <= 50:
                            jj = min(jj, d[i - l][j][kk1] + j ** 2)
                for l in range(1, j):
                    if k <= l * i:
                        jj = min(jj, d[i][l][k] + i ** 2)
                    else:
                        k1 = k - l * i
                        jj = min(jj, d[i][j - l][k1] + i ** 2)
                    if kk <= l * i:
                        if kk <= 50:
                            jj = min(jj, d[i][l][kk] + i ** 2)
                    else:
                        kk1 = kk - l * i
                        if kk1 <= 50:
                            jj = min(jj, d[i][j - l][kk1] + i ** 2)
                d[i][j][k] = jj
for i in range(t):
    (n, m, k) = list(map(int, input().split()))
    jj = d[n][m][k]
    print(jj)
