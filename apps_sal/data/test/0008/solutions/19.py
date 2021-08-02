import sys
a, b, c = sys.stdin.readline().strip().split()
if a == b and b == c:
    print(0)
elif a == b or b == c or a == c:
    print(1)
else:
    na = int(a[0])
    nb = int(b[0])
    nc = int(c[0])
    if (a[1] == b[1] and a[1] == c[1]):
        cp = [na, nb, nc]
        cp.sort()
        cp[0] += 2
        cp[1] += 1
        if (cp[0] == cp[1] and cp[1] == cp[2]):
            print("0")
        elif (cp[0] == cp[1] or cp[1] == cp[2] or cp[0] == cp[1] or (cp[0] + 1) == cp[1] or (cp[1] + 1) == cp[2]):
            print("1")
        else:
            print("2")
    elif(a[1] == b[1]):
        mi = min(na, nb)
        ma = max(na, nb)
        if (mi == (ma - 1) or mi == (ma - 2)):
            print("1")
        else:
            print("2")
    elif(a[1] == c[1]):
        mi = min(na, nc)
        ma = max(na, nc)
        if (mi == (ma - 1) or mi == (ma - 2)):
            print("1")
        else:
            print("2")
    elif(b[1] == c[1]):
        mi = min(nb, nc)
        ma = max(nb, nc)
        if (mi == (ma - 1) or mi == (ma - 2)):
            print("1")
        else:
            print("2")
    else:
        print("2")
