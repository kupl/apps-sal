n, k = list(map(int, input().split()))
mat = []
for i in range(n):
    mat.append(list(input()))
prefr = [[0 for i in range(n)] for j in range(n)]
prefc = [[0 for i in range(n)] for j in range(n)]
done = 0
for i in range(n):
    for j in range(n):
        if j == 0 and mat[i][j] == "B":
            prefr[i][j] = 1
        else:
            prefr[i][j] = prefr[i][j - 1]
            if mat[i][j] == "B":
                prefr[i][j] += 1
        if i == 0 and mat[i][j] == "B":
            prefc[i][j] = 1
        else:
            prefc[i][j] = prefc[i - 1][j]
            if mat[i][j] == "B":
                prefc[i][j] += 1
for i in range(n):
    if prefc[-1][i] == 0:
        done += 1
    if prefr[i][-1] == 0:
        done += 1
dr, dc = [[0 for i in range(n)] for j in range(n)], [[0 for i in range(n)] for j in range(n)]
for j in range(n - k + 1):
    count = []
    s = 0
    for i in range(k):
        if j == 0:
            if prefr[i][-1] - prefr[i][j + k - 1] == 0 and prefr[i][-1] != 0:
                count.append(1)
                s += 1
            else:
                count.append(0)
        else:
            if prefr[i][j - 1] + (prefr[i][-1] - prefr[i][j + k - 1]) == 0 and prefr[i][-1] != 0:
                count.append(1)
                s += 1
            else:
                count.append(0)
    dr[0][j] = s
    # print (count,s)
    for i in range(1, n - k + 1):
        if j == 0:
            if prefr[i + k - 1][-1] - prefr[i + k - 1][j + k - 1] == 0 and prefr[i + k - 1][-1] != 0:
                count.append(1)
                s += 1
            else:
                count.append(0)
        else:
            if prefr[i + k - 1][j - 1] + (prefr[i + k - 1][-1] - prefr[i + k - 1][j + k - 1]) == 0 and prefr[i + k - 1][-1] != 0:
                count.append(1)
                s += 1
            else:
                count.append(0)
        # print (i,j,s)
        if count[i - 1] == 1 and prefr[i - 1][-1] != 0:
            s -= 1
        dr[i][j] = s
# print (dr)
for i in range(n - k + 1):
    count = []
    s = 0
    for j in range(k):
        if i == 0:
            if prefc[-1][j] - prefc[i + k - 1][j] == 0 and prefc[-1][j] != 0:
                count.append(1)
                s += 1
            else:
                count.append(0)
        else:
            if prefc[i - 1][j] + (prefc[-1][j] - prefc[i + k - 1][j]) == 0 and prefc[-1][j] != 0:
                count.append(1)
                s += 1
            else:
                count.append(0)
    dc[i][0] = s
    # print (count,s)
    for j in range(1, n - k + 1):
        if i == 0:
            if prefc[-1][j + k - 1] - prefc[i + k - 1][j + k - 1] == 0 and prefc[-1][j + k - 1] != 0:
                count.append(1)
                s += 1
            else:
                count.append(0)
        else:
            if prefc[i - 1][j + k - 1] + (prefc[-1][j + k - 1] - prefc[i + k - 1][j + k - 1]) == 0 and prefc[-1][j + k - 1] != 0:
                count.append(1)
                s += 1
            else:
                count.append(0)
        # print (i,j,s)
        if count[j - 1] == 1 and prefc[-1][j - 1] != 0:
            s -= 1
        dc[i][j] = s
# print (dc)
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dr[i][j] + dc[i][j])
print(ans + done)
