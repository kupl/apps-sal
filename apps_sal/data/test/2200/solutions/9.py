import math
x = input('').split(' ')
x = [int(y) for y in x]
a = x[0]
b = x[1]
c = x[2]
l = input('').split(' ')
str2 = ''
l = [int(y) for y in l]
for g in range(0, a):
    t = l[g]
    if t * b / c == math.floor(t * b / c):
        str2 = str2 + '0 '
    else:
        ttt = t * b
        equate = math.floor(ttt / c)
        if equate * c % b == 0:
            unawesome = equate * c / b
            str2 = str2 + str(int(t - unawesome))
            str2 = str2 + ' '
        else:
            unawesome = math.floor(equate * c / b) + 1
            str2 = str2 + str(int(t - unawesome))
            str2 = str2 + ' '
print(str2)
