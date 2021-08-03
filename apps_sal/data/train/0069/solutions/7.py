import sys
for _ in range(int(sys.stdin.readline())):
    a = list(map(int, sys.stdin.readline().strip().split(" ")))
    b = sys.stdin.readline().strip()
    n = 0
    inq = False
    s = 0
    if b.count("1") != 0:
        for i in b[b.index("1"):]:
            if i == "1":
                if not inq:
                    inq = True
                    if n != 0:

                        s += min(a[0], n * a[1])
                    else:
                        s += a[0]
                    n = 0
            else:
                inq = False
                n += 1
    print(s)
