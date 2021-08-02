n, k, l = map(int, input().split())
barrels = []
for i in range(n):
    barrels.append([])
    for j in range(k):
        barrels[i].append(-1)
boards = sorted(list(map(int, input().split())))
ans = 0
if boards[n - 1] - boards[0] <= l:
    i = n * k - 1
    ba, bo = n - 1, k
    while boards[i] > boards[0] + l:
        bo -= 1
        if bo == 0:
            ba, bo = ba - 1, k - 1
        barrels[ba][bo] = boards[i]
        i -= 1
    ba, bo = 0, -1
    j = 0
    flag = True
    while j <= i:
        bo += 1
        if bo == k or barrels[ba][bo] != -1:
            ba, bo = ba + 1, 0
            flag = True
        barrels[ba][bo] = boards[j]
        if flag:
            ans += barrels[ba][bo]
            flag = False
        j += 1
print(ans)
