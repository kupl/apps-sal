N = int(input())
Points = [list(map(int, input().split())) for i in range(N)]
# X + Y の偶奇はすべて一致していなければならない
odds_even = set([(x + y) % 2 for x, y in Points])
if len(odds_even) != 1:
    print((-1))
    return

D = [2 ** i for i in range(39)]  # アームの長さ
D = D[::-1]  # 反転
if odds_even == {0}:  # 長さ1のアームを追加
    D.append(1)

print((len(D)))
print((' '.join(map(str, D))))
# 最も長いアームから考える
for tX, tY in Points:
    nX, nY = 0, 0
    ans = ''
    for d in D:
        uX, uY = nX, nY + d  # 上
        rX, rY = nX + d, nY  # 右
        dX, dY = nX, nY - d  # 下
        lX, lY = nX - d, nY  # 左

        diff_U = abs(tX - uX) + abs(tY - uY)
        diff_R = abs(tX - rX) + abs(tY - rY)
        diff_D = abs(tX - dX) + abs(tY - dY)
        diff_L = abs(tX - lX) + abs(tY - lY)

        Diff = [diff_U, diff_R, diff_D, diff_L]
        Command = ['U', 'R', 'D', 'L']
        Next = [[uX, uY], [rX, rY], [dX, dY], [lX, lY]]

        min_diff_index = Diff.index(min(Diff))

        ans += Command[min_diff_index]
        nX, nY = Next[min_diff_index]

    print(ans)

