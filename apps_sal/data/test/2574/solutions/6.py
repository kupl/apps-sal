for _ in range(int(input())):
    n = int(input())
    neg = []
    pos = []
    zero = False
    for e in map(int, input().split()):
        if e < 0:
            neg.append(e)
        elif e > 0:
            pos.append(e)
        else:
            zero = True
    neg.sort()
    pos.sort()
    res = -float("inf")
    if zero:
        res = 0
    for i in range(6): # i = number of -
        if len(neg) < i or len(pos) < 5-i:
            continue
        ar = neg[-i:] + pos[:5-i]
        if i % 2 == 0:
            ar = neg[:i] + pos[-(5-i):]
        #print(i, ar)
        acc = 1
        for e in ar:
            acc *= e
        res = max(res, acc)
    print(res)

