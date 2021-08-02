g = [0] * 5
for i in range(5):
    g[i] = [0] * 5
    g[i] = list(map(int, input().split()))
max = 0
for i in range(5):
    for j in range(5):
        if j != i:
            for m in range(5):
                if m != j and m != i:
                    for n in range(5):
                        if n != m and n != j and n != i:
                            s = 10 - n - m - j - i
                            if g[i][j] + g[j][i] + g[j][m] + g[m][j] + 2 * (g[m][n] + g[n][m]) + 2 * (g[n][s] + g[s][n]) > max:
                                max = g[i][j] + g[j][i] + g[j][m] + g[m][j] + 2 * (g[m][n] + g[n][m]) + 2 * (g[n][s] + g[s][n])
print(max)
