for _ in range(int(input())):
    s = input()
    d = dict()
    d['R'] = 0
    d['S'] = 0
    d['P'] = 0
    d1 = dict()
    d1['R'] = 'P'
    d1['S'] = 'R'
    d1['P'] = 'S'
    for i in s:
        d[i] += 1
    ans = ''
    c = ''
    mx = -1
    for i in list(d.items()):
        if mx < i[1]:
            c = d1[i[0]]
            mx = i[1]
    print(c * len(s))
