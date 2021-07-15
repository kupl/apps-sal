def setPoint(point, a):
    p = point
    x = 0
    y = 0
    if p <= a:
        x = p
        y = 0
    elif p <= a*2:
        x = a
        y = p - a
    elif p <= a*3:
        x = a*3 - p
        y = a
    else:
        x = 0
        y = a*4 - p
    x = int(x*100000)/100000
    y = int(y*100000)/100000
    return str(x) + ' ' + str(y)

a, d = list(map(float, input().split()))
n = int(input())
curP = 0

for l in range(0, n):
    curP += d
    curP = curP % (a*4)
    print(setPoint(curP, a))

