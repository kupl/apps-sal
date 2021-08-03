n = int(input())
l = []
for i in range(n):
    l.append(input())
d = {}
for k in l:
    for i in range(1, 9 + 1):
        for j in range(9 - i + 1):

            a = k[j:j + i]
            z = list(d.keys())
            if a in z:
                if k != d.get(a)[1]:
                    w = d.get(a)
                    w[0] += 1
                    w[1] = k
                    d.update({a: w})
            else:
                d.update({a: [1, k]})
r = list(d.items())
ans = []
for i in r:
    if i[1][0] == 1:
        ans.append([i[0], i[1][1]])
d1 = {}
for i in ans:
    z = list(d1.keys())
    if i[1] in z:
        if len(str(i[0])) < len(str(d1.get(i[1]))):
            d1.update({i[1]: i[0]})
    else:
        d1.update({i[1]: i[0]})
for i in l:
    print(d1.get(i))
