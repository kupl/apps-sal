def candy():
    n = []
    n = input().split()
    N = int(n[0])
    x = int(n[1])
    alist = [int(i) for i in input().split()]

    s = 0
    for i in range(0, N - 1):
        c = int(alist[i])
        d = int(alist[i + 1])
        if int(alist[i] + alist[i + 1]) > x:
            if int(alist[i]) >= x:
                alist[i] = x
                alist[i + 1] = 0
            else:
                alist[i + 1] = int(x - alist[i])
            s += c - int(alist[i]) + d - int(alist[i + 1])
        """
        if int(alist[i]) > x:
            s = s + int(alist[i+1])
            alist[i+1] = 0

        if int(alist[i+1]) + int(alist[i]) > x:
            s = s + (int(alist[i+1]) + int(alist[i]) - x)
            alist[i+1] = x - int(alist[i])
        """
    print(s)


candy()
