a = []
for i in range(8):
    a.append(input())
wmin = 8
bmin = -1
for i in range(8):
    for j in range(8):
        if (a[j][i] == 'W'):
            wmin = min(wmin, j)
            break
        elif (a[j][i] == 'B'):
            break
for i in range(8):
    for j in range(7, 0, -1):
        if (a[j][i] == 'B'):
            bmin = max(bmin, j)
            break
        elif (a[j][i] == 'W'):
            break
if (7 - bmin < wmin):
    print("B")
else:
    print("A")
