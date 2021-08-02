import sys
from collections import deque
from collections import defaultdict
from collections import Counter


def conn(n, m, e):
    d = dict(list(zip(list(range(1, n + 1)), list(range(-1, (-1) * n - 1, -1)))))
    td = defaultdict(lambda: deque([]))  # tdは同値類がキーで中の元が値
    c = 1
    for edge in e:
        a = edge[0]
        b = edge[1]
        da = d[a]  # da,dbはa,bの含まれる同値流のラベル
        db = d[b]
        if da < 0 and db < 0:
            d[a] = c
            d[b] = c
            td[c].append(a)
            td[c].append(b)
            c += 1
        elif da > 0 and db < 0:
            d[b] = da
            td[d[a]].append(b)
        elif da < 0 and db > 0:
            d[a] = db
            td[d[b]].append(a)
        elif da > 0 and db > 0 and da != db:
            for x in td[db]:
                d[x] = da
                td[da].append(x)

    return list(d.values())


def components(n, k, e):
    ed = defaultdict(lambda: deque())
    for edge in e:
        ed[edge[0]].append(edge[1])
    c = 0
    s = [0] * n
    label = [0] * n
    for i in range(1, n + 1):
        if s[i - 1] == 0:
            c += 1
            label[c - 1] = c
            stack = deque([i])
            while stack:
                w = stack.pop()
                s[w - 1] = c
                while ed[w]:
                    wn = ed[w].pop()
                    if s[wn - 1] == 0:
                        s[wn - 1] = c
                        if ed[wn]:
                            stack.append(w)
                            w = wn
                    elif s[wn - 1] < c:
                        label[s[wn - 1] - 1] = c
    return [label[s[i] - 1] for i in range(n)]


def components2(n, k, e):
    ed = defaultdict(lambda: deque())
    for edge in e:
        ed[edge[0]].append(edge[1])
        ed[edge[1]].append(edge[0])
    c = 0
    s = [0] * n
    for i in range(1, n + 1):
        if s[i - 1] == 0:
            c += 1
            stack = deque([i])
            while stack:
                w = stack.pop()
                s[w - 1] = c
                while ed[w]:
                    wn = ed[w].pop()
                    if s[wn - 1] == 0:
                        s[wn - 1] = c
                        if ed[wn]:
                            stack.append(w)
                            w = wn
    return [s[i] for i in range(n)]


def main(n, k, l, e1, e2):
    d1 = components2(n, k, e1)
    d2 = components2(n, l, e2)
    p = tuple(zip(iter(d1), iter(d2)))
    d = Counter(p)
    # print(d1,d2,d,p)
    print((' '.join([str(d[x]) for x in p])))


def __starting_point():
    ssr = sys.stdin.readline
    n, k, l = list(map(int, ssr().strip().split()))
    e1 = []
    e2 = []
    for _ in range(k):
        e1.append(tuple(map(int, ssr().strip().split())))
    for _ in range(l):
        e2.append(tuple(map(int, ssr().strip().split())))
    main(n, k, l, e1, e2)


__starting_point()
