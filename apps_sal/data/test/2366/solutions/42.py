n = int(input())
aaa = list(map(int, input().split(' ')))
hoge = [0, 0]
for i in range(2, int(1000000.0) + 1):
    hoge.append(hoge[i - 1] + (i - 1))
d = {}
for a in aaa:
    d[a] = d.get(a, 0) + 1
total = sum([hoge[v] for v in list(d.values())])
for i in range(1, n + 1):
    ct = d[aaa[i - 1]]
    print(total - (hoge[ct] - hoge[ct - 1]))
