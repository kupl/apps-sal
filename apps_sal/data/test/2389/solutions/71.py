(N, A, B, C) = list(map(int, input().split()))
d = {}
d['A'] = A
d['B'] = B
d['C'] = C
l = [input() for _ in range(N)]
v = A + B + C


def solve():
    res = []
    if v == 0:
        return []
    elif v == 1:
        for i in l:
            (a, b) = i
            if d[a] == 0 and d[b] == 0:
                return []
            elif d[a] > d[b]:
                d[a] -= 1
                d[b] += 1
                res.append(b)
            else:
                d[a] += 1
                d[b] -= 1
                res.append(a)
    else:
        (a, b) = l[0]
        if d[a] == 0 and d[b] == 0:
            return []
        else:
            for (i, j) in enumerate(l):
                (a, b) = j
                if d[a] > d[b]:
                    d[a] -= 1
                    d[b] += 1
                    res.append(b)
                elif d[a] == d[b] == 1 and i + 1 < N:
                    e = set(l[i + 1]) & set([a, b])
                    if len(e) == 1:
                        f = e.pop()
                        g = b if f == a else a
                        d[f] += 1
                        d[g] -= 1
                        res.append(f)
                    else:
                        d[a] -= 1
                        d[b] += 1
                        res.append(b)
                else:
                    d[a] += 1
                    d[b] -= 1
                    res.append(a)
    return res


r = solve()
if r:
    print('Yes')
    for i in r:
        print(i)
else:
    print('No')
