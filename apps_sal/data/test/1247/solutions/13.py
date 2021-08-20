s = input()
n = len(s)
if n % 2 == 1:
    print('First')
else:
    l = [0] * 26
    for i in s:
        if i == 'a':
            l[0] += 1
        elif i == 'b':
            l[1] += 1
        elif i == 'c':
            l[2] += 1
        elif i == 'd':
            l[3] += 1
        elif i == 'e':
            l[4] += 1
        elif i == 'f':
            l[5] += 1
        elif i == 'g':
            l[6] += 1
        elif i == 'h':
            l[7] += 1
        elif i == 'i':
            l[8] += 1
        elif i == 'j':
            l[9] += 1
        elif i == 'k':
            l[10] += 1
        elif i == 'l':
            l[11] += 1
        elif i == 'm':
            l[12] += 1
        elif i == 'n':
            l[13] += 1
        elif i == 'o':
            l[14] += 1
        elif i == 'p':
            l[15] += 1
        elif i == 'q':
            l[16] += 1
        elif i == 'r':
            l[17] += 1
        elif i == 's':
            l[18] += 1
        elif i == 't':
            l[19] += 1
        elif i == 'u':
            l[20] += 1
        elif i == 'v':
            l[21] += 1
        elif i == 'w':
            l[22] += 1
        elif i == 'x':
            l[23] += 1
        elif i == 'y':
            l[24] += 1
        else:
            l[25] += 1
    c = 0
    for i in l:
        if i % 2 == 1:
            c += 1
    if c == 0:
        print('First')
    else:
        print('Second')
