def solve():
    import bisect
    S = input()
    T = input()
    dic = {}
    length = {}

    for i, s in enumerate(S, 1):
        if s not in dic:
            dic[s] = []
        dic[s].append(i)

    for k, v in list(dic.items()):
        if k not in length:
            length[k] = 0
        length[k] = len(v)

    l, turn, prov = len(S), 0, 0

    for t in T:
        if t not in dic:
            print((-1))
            return
        x = bisect.bisect(dic[t], prov)
        if x < length[t]:
            prov = dic[t][x]
        else:
            turn += 1
            prov = dic[t][0]
    print((turn * l + prov))


solve()
