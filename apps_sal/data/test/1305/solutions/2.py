n = int(input())
ms = [int(x) for x in input().split()]
yes = True
a = b = 0
s = 0
for m in ms:
    if m == 25:
        a += 1
    elif m == 50:
        a -= 1
        b += 1
    elif m == 100:
        if b > 0:
            b -= 1
            a -= 1
        else:
            a -= 3
    if a < 0 or b < 0:
        yes = False
        break
if yes:
    print('YES')
else:
    print('NO')
