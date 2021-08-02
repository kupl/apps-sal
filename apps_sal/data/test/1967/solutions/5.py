def mash(pole):
    ans = []
    for i in range(len(pole)):
        s = pole[i]
        new = ''
        for i in s:
            new += (i * 2)
        ans.append(new)
        ans.append(new)
    return ans


def change(pole, a, b):
    x = len(pole[0]) % 2
    fir = []
    sec = []
    new = []
    for i in range(b):
        s = ''
        for j in range(a):
            s += pole[j][i]
        if i + 1 <= len(pole[0]) // 2:
            fir.append(s)
            continue
        if i + 1 >= (len(pole[0]) // 2 + x):
            sec.append(s)
    for i in range(len(sec[0])):
        s = ''
        for j in range(len(sec) + len(fir)):
            if j < len(sec):
                s += sec[j][i]
            else:
                s += fir[j - len(sec)][i]
        new.append(s)
    return new


def pov(pole, a, b):
    new = []
    for i in range(a):
        s = ''
        for j in range(b):
            s += pole[j][i]
        new.append(s)
    return new


a, b = list(map(int, input().split()))
pole = []
for i in range(b):
    s = input()
    pole.append(s)
new = mash(pov(pole, a, b))
for i in new:
    print(i)
