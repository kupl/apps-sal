n, x = [int(v) for v in input().split()]
a = [int(v) for v in input().split()]

sa = set(a)

if len(sa) < n:
    print(0)
else:
    la = [v & x for v in a if v & x != v]
    if set(la) & sa:
        print(1)
    else:
        if len(set(la)) < len(la):
            print(2)
        else:
            print(-1)

