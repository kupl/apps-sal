n, p = list(map(int, input().split()))
if p == 0:
    dv = str(bin(n))[2:]
    colvo = dv.count("1")
    print(colvo)
else:
    m = 1
    while n - m * p >= 0:
        # print(m)
        a = n - m * p
        dv = str(bin(a))[2:]
        colvo = dv.count("1")
        if colvo <= m and m <= a:
            print(m)
            return
        m += 1
    print(-1)
