
a, b = input().split()
horiz = int(a)
vert = int(b)

if horiz > vert:
    if vert % 2 == 0:
        print('Malvika')
    else:
        print('Akshat')
elif horiz < vert:
    if horiz % 2 == 0:
        print('Malvika')
    else:
        print('Akshat')
elif horiz == vert:
    if vert % 2 == 0:
        print('Malvika')
    else:
        print('Akshat')
