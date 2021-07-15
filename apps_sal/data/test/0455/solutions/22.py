# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]

# x + y のパリティが同一かチェック, 異なる座標が存在する場合は実現不可能
p = set()
for i in range(N):
    p.add((XY[i][0] + XY[i][1]) % 2)
if len(p) > 1:
    print((-1))
    return

# 腕の長さを1,2,4,8... で考えると, パリティ1を実現できる.
# 与えられた座標のパリティが0の場合, X座標を-1し, パリティ1の場合に帰着する(あとでX+1する)
if 0 in p:
    for i in range(N):
        XY[i][0] -= 1

# アームを準備
D = []
for i in range(35):
    D.append(2**i)
D.sort(reverse=True)

Ans = []
# 順番に計算
for i in range(N):
    x,y = XY[i][0],XY[i][1]
    x0,y0 = 0,0
    ans = ""
    # 原点を中心にX字で分割される領域の (上下左右) どちらかを判断し, 移動させ, 都度原点を調整
    for d in D:
        dx,dy = x-x0,y-y0
        # 右
        if dy < dx and dy > -dx:
            ans += "R"
            x0 += d
        # 下
        elif dy < dx and dy < -dx:
            ans += "D"
            y0 -= d
        # 左
        elif dy > dx and dy < -dx:
            ans += "L"
            x0 -= d
        # 上
        else:
            ans += "U"
            y0 += d
    Ans.append(ans)

# パリティが 0 の場合 : 長さ1のアームを追加, X座標を -1 した分を +1 して調整(つまり最後に "R" を追加する)
if 0 in p:
    D.append(1)
    print((len(D)))
    print((" ".join(map(str,D))))
    for ans in Ans:
        print((ans + "R"))
# パリティが 1 の場合 : そのまま出力
else:
    print((len(D)))
    print((" ".join(map(str,D))))
    for ans in Ans:
        print(ans)




