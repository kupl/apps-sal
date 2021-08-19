def __starting_point():
    n = int(input())
    visitors = set()
    basevisitors = set()
    log = []
    for _ in range(n):
        (sign, ID) = input().split()
        log.append((sign, ID))
        if sign == '+':
            visitors.add(ID)
        elif ID in visitors:
            visitors.remove(ID)
        else:
            basevisitors.add(ID)
    res = len(basevisitors)
    for aLog in log:
        if aLog[0] == '+':
            basevisitors.add(aLog[1])
            res = max(res, len(basevisitors))
        else:
            basevisitors.remove(aLog[1])
    print(res)


__starting_point()
