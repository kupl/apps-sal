import collections as col
n = int(input())
v = list(map(int, input().split()))
o = col.Counter(v[0:n:2])
e = col.Counter(v[1:n:2])
ook = o.most_common()
eok = e.most_common()
ok = ook[0][1] + eok[0][1]
if ook[0][0] == eok[0][0]:
    if len(ook) < 2 and len(eok) < 2:
        print(n // 2)
        return
    elif len(ook) < 2:
        ok = ook[0][1] + eok[1][1]
    elif len(eok) < 2:
        ok = ook[1][1] + eok[0][1]
    else:
        ok = max(ook[0][1] + eok[1][1], ook[1][1] + eok[0][1])
print(n - ok)
