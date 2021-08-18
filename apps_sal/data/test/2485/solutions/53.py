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

tmpX = indexW[0]
tmpY = indexH[0]

flag = 0


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
