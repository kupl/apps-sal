import math

n, a, b = map(int, input().split())
xlist = [int(x) for x in input().split()]
savestring = ''

for i in range(n):
    maxmoney = math.floor(xlist[i] * a / b)
    saves = xlist[i] - math.ceil(maxmoney * b / a)
    savestring += str(saves) + ' '

print(savestring)
