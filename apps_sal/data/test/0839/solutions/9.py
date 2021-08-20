g = []
for i in range(5):
    g.append(list(map(int, input().split())))
max = 0
for i in range(5):
    for j in range(5):
        if i != j:
            for k in range(5):
                if i != k and j != k:
                    for l in range(5):
                        if i != l and j != l and (k != l):
                            m = 10 - i - j - k - l
                            sum = g[i][j] + g[j][i] + g[j][k] + g[k][j]
                            sum += 2 * (g[k][l] + g[l][k] + g[l][m] + g[m][l])
                            if sum > max:
                                max = sum
print(max)
