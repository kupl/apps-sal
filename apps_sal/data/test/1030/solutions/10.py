from sys import stdin


def main():
    a = stdin.readline().split()
    b = int(a[0])
    c = int(a[1])
    d = int(a[2])
    e = []
    g = str(c)
    k = []
    if (c == 1):
        e = e
    elif (c > 1) and ((c - d) > 1):
        e.append('<<')
        for i in range(d):
            e.append(str(c - d + i))
    elif (c - d == 1):
        for i in range(d):
            e.append(str(c - d + i))
    elif ((c - d) < 1):
        j = 2
        i = 0
        while (j > 1):
            j = c - i - 1
            k.append(j)
            i = i + 1
        k.sort()
        for i in range(len(k)):
            k[i] = str(k[i])
        e = k + e
    f = str('(' + g + ')')
    e.append(f)

    if ((c + d) == b):
        for i in range(d):
            e.append(str(c + i + 1))
    elif(c == b):
        e = e
    elif ((c + d) > b):
        j = 1
        i = 0
        while (j < b):
            j = (c + i + 1)
            e.append(str(j))
            i = i + 1
    elif (c < b) and ((c + d) < b):
        for i in range(d):
            e. append(str(c + i + 1))
        e.append('>>')
    h = ' '.join(e)
    print(h)


main()
