s = input()

atd = ''
tpd = ''
for i, t in enumerate(s):

    if t == 'g':
        tpd += '0'
    else:
        tpd += '1'

    if i % 2 == 0:
        atd += '0'
    else:
        atd += '1'

point = 0
for a, t in zip(atd, tpd):

    x = int(a) - int(t)

    if x == 1:
        point += 1
    elif x == -1:
        point -= 1


print(point)
