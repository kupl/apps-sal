import collections
n = int(input())
ss = sorted([input() for i in range(n)], key=lambda x: len(x))
s = ss[0]
poplist = []
cc = collections.Counter(s)

for i in range(1, n):
    for c in cc:
        if c in ss[i]:
            cc[c] = min(cc[c], ss[i].count(c))
        else:
            if c not in poplist:
                poplist.append(c)

for p in poplist:
    dd = cc.pop(p)

ans = [x[0] * x[1] for x in cc.items()]
ans = ''.join(sorted(ans))
print(ans)
