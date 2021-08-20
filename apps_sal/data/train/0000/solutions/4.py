t = int(input())
for i in range(t):
    n = int(input())
    (i0, i1) = ([], [])
    (l0, l1) = ([], [])
    (h0, h1) = (False, False)
    for i in range(n):
        t = input()
        if t[0] == '0' and t[-1] == '1':
            i0.append(i)
            l0.append(t)
        elif t[0] == '1' and t[-1] == '0':
            i1.append(i)
            l1.append(t)
        elif t[0] == t[-1] == '1':
            h1 = True
        elif t[0] == t[-1] == '0':
            h0 = True
    (c0, c1) = (len(l0), len(l1))
    (req, sl) = (0, [])
    s0 = set(l0)
    s1 = set(l1)
    if c0 > 0 or c1 > 0:
        if c0 - c1 > 1:
            req = (c0 - c1) // 2
            sel = 0
            sl = []
            for tt in range(len(l0)):
                t = l0[tt]
                if not t[::-1] in s1:
                    req -= 1
                    sl.append(i0[tt] + 1)
                if req == 0:
                    break
        elif c1 - c0 > 1:
            req = (c1 - c0) // 2
            sel = 0
            sl = []
            for tt in range(len(l1)):
                t = l1[tt]
                if not t[::-1] in s0:
                    req -= 1
                    sl.append(i1[tt] + 1)
                if req == 0:
                    break
        if req > 0:
            print(-1)
        else:
            print(len(sl))
            print(*sl)
    elif h0 and h1:
        print(-1)
    else:
        print(0)
        print(*[])
