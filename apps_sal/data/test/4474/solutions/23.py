for _ in range(int(input())):
    n = int(input())
    l = []
    j = -1
    while (n):
        temp1 = n % 3
        n = n // 3
        if (temp1 == 2):
            temp1 = 0
            j = len(l)
        l.append(temp1)
    l.append(0)
    # print(l, j)
    if (j != -1):
        for i in range(j):
            l[i] = 0
        l[j + 1] += 1
        while (l[j + 1] == 2):
            j = j + 1
            l[j] = 0
            l[j + 1] += 1
    # print(l)
    s = ''
    for i in l[::-1]:
        s += str(i)
    print(int(s, 3))
