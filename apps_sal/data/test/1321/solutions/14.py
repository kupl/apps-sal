n = int(input())
maxW = 0
widthes = []
heigthes = []
for i in range(n):
    w, h = map(int, input().split())
    maxW += w
    widthes.append(w)
    heigthes.append(h)
maxH = max(heigthes)
indexMaxH = heigthes.index(maxH)
for i in range(n):
    if i == indexMaxH:
        el = heigthes.pop(i)
        maxH2 = max(heigthes)
        heigthes.insert(i, el)
        print((maxW - widthes[i]) * maxH2, end=" ")
    else:
        print((maxW - widthes[i]) * maxH, end=" ")
