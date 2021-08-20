N = int(input())


def ceildiv(x, y):
    if x % y == 0:
        return x // y
    else:
        return x // y + 1


for _ in range(N):
    doms = []
    (oc, zc) = (0, 0)
    n = int(input())
    used = set()
    fulls = dict()
    for i in range(n):
        d = input()
        used.add(d)
        if d[0] != d[-1]:
            fulls[i] = d
            doms.append((i, (d[0], d[-1])))
        elif d[0] == '0':
            zc = 1
        else:
            oc = 1
    if len(doms) == 0:
        if zc == 1 and oc == 1:
            print(-1)
        else:
            print(0)
    else:
        _01 = 0
        _10 = 0
        _01_indexes = []
        _10_indexes = []
        for dom in doms:
            if dom[1] == ('0', '1'):
                _01 += 1
                _01_indexes.append(dom[0])
            else:
                _10 += 1
                _10_indexes.append(dom[0])
        if _10 < _01:
            (_01, _10) = (_10, _01)
            (_01_indexes, _10_indexes) = (_10_indexes, _01_indexes)
        _10_indexes = [x for x in _10_indexes if fulls[x][::-1] not in used]
        need = ceildiv(_10 - _01 - 1, 2)
        if len(_10_indexes) >= need:
            print(need)
            print(' '.join(list([str(x + 1) for x in _10_indexes[:need]])))
        else:
            print(-1)
