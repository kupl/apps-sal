n, k, q = list(map(int, input().split()))

t = [0] + list(map(int, input().split()))

ts = list()

for i in range(q):
    typ, idi = list(map(int, input().split()))
    if typ == 1:
        cnt = len(ts)
        tl = t[idi]
        if (cnt < k):
            ts.append(tl)
        else:
            if (ts[0] < tl):
                del ts[0]
                ts.append(tl)
        ts.sort()
    elif typ == 2:
        if t[idi] in ts:
            print("YES")
        else:
            print("NO")
