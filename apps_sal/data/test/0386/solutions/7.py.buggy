n = int(input(''))
z = {}
ch = {}
tf = {}
for i in range(0, n):
    z[i], ch[i], tf[i] = list(map(str, input('').split()))
    ch[i] = int(ch[i])
    if z[i] == '<':
        z[i] = int(1)
    if z[i] == '<=':
        z[i] = int(2)
    if z[i] == '>':
        z[i] = int(3)
    if z[i] == '>=':
        z[i] = int(4)
    if tf[i] == 'N':
        if z[i] == 1:
            z[i] = 4
        else:
            if z[i] == 2:
                z[i] = 3
            else:
                if z[i] == 3:
                    z[i] = 2
                else:
                    if z[i] == 4:
                        z[i] = 1
    if z[i] == 1:
        tf[i] = ch[i] - 1
    if z[i] == 3:
        tf[i] = ch[i] + 1
    if ((z[i] == 2) or (z[i] == 4)):
        tf[i] = ch[i]


def proverka(x, znak, oo):
    if znak == 1:
        if x < oo:
            return 1
        else:
            return 0
    elif znak == 2:
        if x <= oo:
            return 1
        else:
            return 0
    elif znak == 3:
        if x > oo:
            return 1
        else:
            return 0
    elif znak == 4:
        if x >= oo:
            return 1
        else:
            return 0


for i in range(0, n):
    l = 1
    for j in range(0, n):
        l *= proverka(tf[i], z[j], ch[j])
        if (l == 0):
            break
    if l == 1:
        print(tf[i])
        return
print("Impossible")
