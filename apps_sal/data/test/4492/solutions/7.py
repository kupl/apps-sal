def candy():
    boxNum, x = [int(i) for i in input().split()]
    ain = input()
    alist = ain.split(' ')

    s = 0

    for i in range(0, boxNum - 1):
        if int(alist[i + 1]) + int(alist[i]) > x:
            s = s + (int(alist[i + 1]) + int(alist[i]) - x)
            alist[i + 1] = x - int(alist[i])
            if int(alist[i + 1]) < 0:
                alist[i] = int(alist[i]) + int(alist[i + 1])
                alist[i + 1] = 0

    print(s)


candy()
