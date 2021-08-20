g = [list(map(int, input().split())) for i in range(5)]
ans = 0
for i1 in range(5):
    for i2 in range(5):
        for i3 in range(5):
            for i4 in range(5):
                for i5 in range(5):
                    if i1 != i2 and i3 != i1 and (i3 != i2) and (i4 != i1) and (i4 != i2) and (i4 != i3) and (i5 != i1) and (i5 != i2) and (i5 != i3) and (i5 != i4):
                        ans = max(ans, g[i1][i2] + g[i2][i1] + g[i3][i4] + g[i4][i3] + g[i2][i3] + g[i3][i2] + g[i4][i5] + g[i5][i4] + g[i3][i4] + g[i4][i3] + g[i4][i5] + g[i5][i4])
print(ans)
