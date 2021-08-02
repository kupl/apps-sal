t = int(input())


def change(p, dct):
    if dct[p] == 1:
        return [p, 0]
    for j in range(4):
        for i in range(10):
            nw = list(p[:])
            nw[j] = str(i)
            nw = ''.join(nw)
            if nw not in dct:
                return [nw, 1]


for _ in range(t):
    n = int(input())
    l = {}
    pins = []
    for i in range(n):
        s = input()
        pins.append(s)
        if s in l:
            l[s] += 1
        else:
            l[s] = 1
    res = []
    cnt = 0
    for p in pins:
        c, d = change(p, l)
        cnt += d
        l[p] -= 1
        if l[p] == 0:
            del l[p]
        if c not in l:
            l[c] = 1
        else:
            l[c] += 1
        res.append(c)
    print(cnt)
    for i in res:
        print(i)
