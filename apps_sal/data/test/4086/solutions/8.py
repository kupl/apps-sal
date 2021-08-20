n = int(input())
L = list(map(int, input().split()))
m = dict()
for x in L:
    m.setdefault(x, 0)
    m[x] += 1
res = []
for x in L:
    m[x] -= 1
    if m[x] == 0:
        res.append(x)
print(len(res))
print(' '.join(map(str, res)))
