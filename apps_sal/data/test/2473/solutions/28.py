n, k = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(n)]
XY.sort(key=lambda x: x[0])
XY = [xy + [x] for x, xy in enumerate(XY)]
XY.sort(key=lambda x: x[1])
XY = [xy + [y] for y, xy in enumerate(XY)]

gr = [[0] * n for _ in range(n)]
for _, _, i, j in XY:
    gr[i][j] = 1

rui = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        rui[i + 1][j + 1] = rui[i + 1][j] + rui[i][j + 1] - rui[i][j] + gr[i][j]

# XYの2点,3点,4点を総当たり
ans = 10 ** 21
for i in range(n - 1):
    for j in range(i + 1, n):
        x = [XY[m][0] for m in [i, j]]
        y = [XY[m][1] for m in [i, j]]
        ii = [XY[m][2] for m in [i, j]]
        jj = [XY[m][3] for m in [i, j]]
        innerPoints = rui[max(ii) + 1][max(jj) + 1] \
            + rui[min(ii)][min(jj)] \
            - rui[min(ii)][max(jj) + 1] \
            - rui[max(ii) + 1][min(jj)]
        if innerPoints >= k:
            area = (max(x) - min(x)) * (max(y) - min(y))
            if area < ans:
                ans = area

if n > 2:
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for l in range(j + 1, n):
                x = [XY[m][0] for m in [i, j, l]]
                y = [XY[m][1] for m in [i, j, l]]
                ii = [XY[m][2] for m in [i, j, l]]
                jj = [XY[m][3] for m in [i, j, l]]
                innerPoints = rui[max(ii) + 1][max(jj) + 1] \
                    + rui[min(ii)][min(jj)] \
                    - rui[min(ii)][max(jj) + 1] \
                    - rui[max(ii) + 1][min(jj)]
                if innerPoints >= k:
                    area = (max(x) - min(x)) * (max(y) - min(y))
                    if area < ans:
                        ans = area

if n > 3:
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for l in range(j + 1, n - 1):
                for o in range(l + 1, n):
                    x = [XY[m][0] for m in [i, j, o, l]]
                    y = [XY[m][1] for m in [i, j, o, l]]
                    ii = [XY[m][2] for m in [i, j, o, l]]
                    jj = [XY[m][3] for m in [i, j, o, l]]
                    innerPoints = rui[max(ii) + 1][max(jj) + 1] \
                        + rui[min(ii)][min(jj)] \
                        - rui[min(ii)][max(jj) + 1] \
                        - rui[max(ii) + 1][min(jj)]
                    if innerPoints >= k:
                        area = (max(x) - min(x)) * (max(y) - min(y))
                        if area < ans:
                            ans = area

print(ans)
