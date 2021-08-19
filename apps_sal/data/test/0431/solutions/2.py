def sol():
    (n, m) = map(int, input().split(' '))
    mapp = []
    for a in range(n):
        s = list(input())
        s = [c == '1' for c in s]
        mapp.insert(0, s[1:-1])
    res = None
    empty_floor = n
    while True:
        litup = False
        for x in mapp[empty_floor - 1]:
            if x:
                litup = True
                break
        if not litup:
            empty_floor -= 1
        else:
            break
        if empty_floor < 0:
            break
    if empty_floor <= 0:
        return 0
    for comb in range(2 ** (empty_floor - 1)):
        temp = 0
        c = bin(comb)[2:]
        c = '0' * (empty_floor - 1 - len(c)) + c
        c = list(c)
        c = [x == '1' for x in c]
        last = False
        if empty_floor != 1:
            for (i, x) in enumerate(c):
                if x != last:
                    temp += m + 1 + 1
                else:
                    f = None
                    for (j, y) in enumerate(mapp[i]):
                        if y:
                            f = j
                            if last:
                                break
                    if f is None:
                        temp += 1
                    elif last:
                        temp += 2 * (m - f) + 1
                    else:
                        temp += 2 * (f + 1) + 1
                last = x
        f = None
        for (j, y) in enumerate(mapp[empty_floor - 1]):
            if y:
                f = j
                if last:
                    break
        if f is not None:
            if c[-1]:
                temp += m - f
            else:
                temp += f + 1
        if res is None:
            res = temp
        res = min(res, temp)
    return res


print(sol())
