a = []

b = []
b.append(3)
b.append(3)
b.append(0)
b.append(4)
b.append(4)
b.append(0)
b.append(3)
b.append(3)
a.append(b)
b = []
b.append(3)
b.append(3)
b.append(0)
b.append(4)
b.append(4)
b.append(0)
b.append(3)
b.append(3)
a.append(b)
b = []
b.append(2)
b.append(2)
b.append(0)
b.append(3)
b.append(3)
b.append(0)
b.append(2)
b.append(2)
a.append(b)
b = []
b.append(2)
b.append(2)
b.append(0)
b.append(3)
b.append(3)
b.append(0)
b.append(2)
b.append(2)
a.append(b)
b = []
b.append(1)
b.append(1)
b.append(0)
b.append(2)
b.append(2)
b.append(0)
b.append(1)
b.append(1)
a.append(b)
b = []
b.append(1)
b.append(1)
b.append(0)
b.append(2)
b.append(2)
b.append(0)
b.append(1)
b.append(1)
a.append(b)
max = 0
a1 = []
pos1 = 0
pos2 = 0
for i in range(6):
    str = input()
    for i1 in range(8):
        if (str[i1] == '.' and a[i][i1] > max):
            max = a[i][i1]
            pos1 = i
            pos2 = i1
    a1.append(str)
for i in range(6):
    for i1 in range(8):
        if (i == pos1 and i1 == pos2):
            print('P', end='')
        else:
            print(a1[i][i1], end='')
    print()
