from itertools import groupby
(n, a, b, k) = map(int, input().split())
s = input()
sg = [list(g) for (s, g) in groupby(s)]
ll = 0
hits = []
for i in range(0, len(sg)):
    if sg[i][0] == '0' and len(sg[i]) >= b:
        for hit in range(b - 1, len(sg[i]), b):
            hits.append(hit + ll + 1)
        ll += len(sg[i])
    else:
        ll += len(sg[i])
hits = hits[a - 1:]
print(len(hits))
print(*hits)
'\n\n13 3 2 3\n1000000010001\n\n\n15 3 2 3\n1000000000010001\n\n'
