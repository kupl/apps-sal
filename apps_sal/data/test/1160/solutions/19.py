contest = True
if not contest:
    fin = open('in', 'r')
inp = input if contest else lambda: fin.readline()[:-1]


def read():
    return tuple(map(int, inp().split()))


tz = dict([(v, i) for (i, v) in enumerate('S,M,L,XL,XXL,XXXL'.split(','))])
sz = list(read())
n = read()[0]


def main():
    ans = {}
    q = []
    for i in range(n):
        v = inp().split(',')
        if len(v) == 1:
            v = v[0]
            ans[i] = v
            sz[tz[v]] -= 1
            if sz[tz[v]] < 0:
                return ['NO']
        else:
            v = sorted([(tz[e], e, i) for e in v], key=lambda v: v[0])
            q += [v]
    q.sort(key=lambda v: v[0][0])
    for v in q:
        if sz[v[0][0]] <= 0:
            if sz[v[1][0]] <= 0:
                return ['NO']
            else:
                sz[v[1][0]] -= 1
                ans[v[1][2]] = v[1][1]
        else:
            sz[v[0][0]] -= 1
            ans[v[0][2]] = v[0][1]
    return ['YES', [ans[i] for i in range(n)]]


v = main()
print(v[0])
if len(v) > 1:
    print('\n'.join(v[1]))
