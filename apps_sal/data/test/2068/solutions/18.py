def r(d, key):
    if key in d:
        s = 0
        for i in d[key]:
            m = r(d, i)
            if m > s: s = m
        return s + 1
    else: return 1


def size(d):
    s = 0
    for i in d:
        m = r(d, i)
        if m > s: s = m
    return s


n = int(input())
a = [input().lower().split() for i in range(n)]
d = {}
for i in a:
    d[i[2]] = []
for i in a:
    d[i[2]].append(i[0])
s = size(d)
print(s)
