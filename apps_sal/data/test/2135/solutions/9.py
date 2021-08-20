(h, w) = list(map(int, input().split()))
mp = []
mp.append(list('#' * (w + 2)))
for i in range(h):
    mp.append(list(input()))
    mp[i + 1].insert(0, '#')
    mp[i + 1].append('#')
mp.append(list('#' * (w + 2)))
mpV = []
mpH = []
mpV.append([])
mpH.append([])
for i in range(w + 2):
    mpV[0].append(0)
    mpH[0].append(0)
for i in range(1, h + 2):
    mpV.append([])
    mpH.append([])
    mpV[i].append(0)
    mpH[i].append(0)
    for j in range(1, w + 2):
        mpV[i].append(mpV[i][j - 1] + mpV[i - 1][j] - mpV[i - 1][j - 1] + (1 if mp[i][j] == '.' and mp[i + 1][j] == '.' else 0))
        mpH[i].append(mpH[i][j - 1] + mpH[i - 1][j] - mpH[i - 1][j - 1] + (1 if mp[i][j] == '.' and mp[i][j + 1] == '.' else 0))
anc = []
n = int(input())
for k in range(n):
    (y0, x0, y1, x1) = list(map(int, input().split()))
    A = mpV[y0 - 1][x0 - 1] + mpV[y1 - 1][x1] - mpV[y1 - 1][x0 - 1] - mpV[y0 - 1][x1]
    A += mpH[y0 - 1][x0 - 1] + mpH[y1][x1 - 1] - mpH[y1][x0 - 1] - mpH[y0 - 1][x1 - 1]
    anc.append(A)
for k in range(n):
    print(anc[k])
