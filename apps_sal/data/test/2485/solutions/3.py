(H, W, M) = map(int, input().split())
width = [0] * W
height = [0] * H
st = set()
for i in range(M):
    (y, x) = map(int, input().split())
    st.add((x - 1, y - 1))
    width[x - 1] += 1
    height[y - 1] += 1
maxW = max(width)
maxH = max(height)
indexW = [i for (i, v) in enumerate(width) if v == maxW]
indexH = [i for (i, v) in enumerate(height) if v == maxH]
ans = maxW + maxH
tempX = indexW[0]
tempY = indexH[0]
flag = False
for x in indexW:
    y = tempY
    if not (x, y) in st:
        flag = True
        break
for y in indexH:
    x = tempX
    if not (x, y) in st:
        flag = True
        break
if flag:
    print(ans)
else:
    print(ans - 1)
