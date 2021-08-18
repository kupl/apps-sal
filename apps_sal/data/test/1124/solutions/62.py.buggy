n = int(input())
l = [int(x) for x in input().split()]

while True:
    l = list(set(l))
    if len(l) == 1:
        print((l[0]))
        return

    mn = min(l)
    for i, e in enumerate(l):
        if e == mn:
            pass
        else:
            if mn == 1:
                l[i] = 1
            else:
                if e % mn == 0:
                    l[i] = mn
                else:
                    l[i] = e % mn
