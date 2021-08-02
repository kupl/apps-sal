H, W, M = list(map(int, input().split()))
width = [0] * W
height = [0] * H

st = set()
for i in range(M):
    y, x = list(map(int, input().split()))
    st.add((x - 1, y - 1))
    width[x - 1] += 1
    height[y - 1] += 1

maxW = max(width)
maxH = max(height)

indexW = [i for i, v in enumerate(width) if v == maxW]
indexH = [i for i, v in enumerate(height) if v == maxH]

ans = maxW + maxH

# それぞれ列と行の最大値の中から適当に１つずつ列と行を選ぶ
tmpX = indexW[0]
tmpY = indexH[0]

# HeightとWidthのそれぞれの最大値の点(x, y)に爆弾がない場合があるかどうか
flag = 0

#print(f"indexH {indexH}")
#print(f"indexW {indexW}")

# Heightの最大値と、widthのそれぞれを全探索
for x in indexW:
    y = tmpY
    if not (x, y) in st:
        flag = 1
        break


for y in indexH:
    x = tmpX
    if not (x, y) in st:
        flag = 1
        break

if flag == 1:
    print(ans)
else:
    print((ans - 1))
