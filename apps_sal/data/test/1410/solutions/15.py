from collections import defaultdict as dd

n = int(input())
c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))

c1 = [None] + c1
c2 = [None] + c2
c3 = [None] + c3
c = [[None for _ in range(n + 1)]] + [c1] + [c2] + [c3]

d = dd(lambda: [])

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    d[a].append(b)
    d[b].append(a)

flag = True
root = None
for i in range(1, n + 1):
    if len(d[i]) == 1:
        root = i
    if len(d[i]) >= 3:
        flag = False

if not flag:
    print(-1)
else:
    l1, l2, l3 = [], [], []

    q = [(root, 1)]
    s = set()

    while q:
        node, lv = q.pop(0)

        if node not in s:
            s.add(node)
            if lv == 1:
                l1.append(node)
            elif lv == 2:
                l2.append(node)
            elif lv == 3:
                l3.append(node)

            for v in d[node]:
                if lv == 1:
                    q.append((v, 2))
                elif lv == 2:
                    q.append((v, 3))
                elif lv == 3:
                    q.append((v, 1))

    _min = 1e114 + 1
    cl = (0, 0, 0)

    for (cl1, cl2, cl3) in [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]:
        cost = sum([c[cl1][j] for j in l1]) + sum([c[cl2][j] for j in l2]) + sum([c[cl3][j] for j in l3])
        if cost < _min:
            _min = cost
            cl = (cl1, cl2, cl3)

    print(int(_min))
    cl1, cl2, cl3 = cl
    cl = [(i, cl1) for i in l1] + [(i, cl2) for i in l2] + [(i, cl3) for i in l3]
    cl.sort(key=lambda x: x[0])
    cl = [j for i, j in cl]
    print(*cl)
