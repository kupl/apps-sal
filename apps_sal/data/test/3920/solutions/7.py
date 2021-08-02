import math


def getarea(a):
    return (a * a * math.sqrt(3)) / 8


x = input("").split(' ')
x = [int(y) for y in x]
a1 = x[0]
a2 = x[1]
a3 = x[2]
a4 = x[3]
a5 = x[4]
a6 = x[5]
if (a2 == a5):
    totarea = (a1 / 2 + a3 / 2 + a2) * ((a3 * math.sqrt(3) / 2) + (a4 * math.sqrt(3) / 2))
    totarea -= getarea(a3) + getarea(a4) + getarea(a1) + getarea(a6)
    print((int)(((4 * totarea) / math.sqrt(3)) + 0.5))
elif (a3 == a6):
    totarea = (a2 / 2 + a4 / 2 + a3) * ((a4 * math.sqrt(3) / 2) + (a5 * math.sqrt(3) / 2))
    totarea -= getarea(a4) + getarea(a5) + getarea(a1) + getarea(a2)
    print((int)(((4 * totarea) / math.sqrt(3)) + 0.5))
else:
    totarea = (a6 / 2 + a2 / 2 + a1) * ((a2 * math.sqrt(3) / 2) + (a3 * math.sqrt(3) / 2))
    totarea -= getarea(a2) + getarea(a3) + getarea(a5) + getarea(a6)
    print((int)(((4 * totarea) / math.sqrt(3)) + 0.5))
