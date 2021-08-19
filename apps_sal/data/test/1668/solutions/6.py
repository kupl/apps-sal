t = int(input())
for i in range(t):
    n = int(input())
    p = []
    s = []
    d = {}
    for j in range(n):
        st = input()
        s.append(st)
        p.append(list(map(int, list(st))))
        if st in list(d.keys()):
            d[st].append(j)
        else:
            d[st] = [j]
    poss = [i for i in range(10)]
    for j in range(n):
        poss[p[j][0]] = -1
    rest = [x for x in poss if x != -1]
    r_i = 0
    res = 0
    for k in list(d.keys()):
        if len(d[k]) > 1:
            for r in d[k][1:]:
                p[r][0] = rest[r_i]
                r_i += 1
                res += 1
    print(res)
    for o in p:
        print(''.join(map(str, o)))
