n = int(input())
d = dict()


def ppp(d):
    for (k, v) in list(d.items()):
        print(k, ':', v.s, ':', id(v))
    print('-----')


class A:

    def __init__(self):
        self.s = []


for _ in range(n - 1):
    (a, b) = list(map(int, input().split()))
    if a not in d and b not in d:
        t = A()
        t.s.append(a)
        t.s.append(b)
        d[a] = t
        d[b] = t
    elif a in d and b not in d:
        d[a].s.append(b)
        d[b] = d[a]
    elif a not in d and b in d:
        d[b].s.append(a)
        d[a] = d[b]
    else:
        d[a].s.extend(d[b].s)
        for x in d[b].s:
            d[x] = d[a]
print(*d[1].s)
