n = int(input())
sez = [0, 0, 0]
kvenka = [int(i) for i in input().split()]
prej = True
for i in range(n):
    temp = kvenka[i]
    if temp == 25:
        sez[0] += 1
    elif temp == 50:
        sez[1] += 1
        sez[0] -= 1
    else:
        sez[2] += 1
        if sez[1] > 0:
            sez[0] -= 1
            sez[1] -= 1
        else:
            sez[0] -= 3

    ok = True
    for i in range(3):
        if sez[i] < 0:
            ok = False

    if not ok:
        prej = False
        break

if prej:
    print("YES")
else:
    print("NO")
