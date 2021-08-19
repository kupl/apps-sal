from itertools import product
n = int(input())
d = {}
for i in range(n):
    a = int(input())
    for _ in range(a):
        (x, y) = map(int, input().split())
        if i + 1 not in d:
            d[i + 1] = []
        d[i + 1].append((x, y))
ret = 0
for x in product((0, 1), repeat=n):
    tmp = [-1] * n
    ok = True
    for i in range(n):
        if x[i] == 1 and i + 1 in d:
            for y in d[i + 1]:
                if tmp[y[0] - 1] == -1:
                    tmp[y[0] - 1] = y[1]
                elif tmp[y[0] - 1] != y[1]:
                    ok = False
                    break
        if not ok:
            break
    if ok and all((a == b or b == -1 for (a, b) in zip(x, tmp))):
        ret = max(ret, sum(x))
print(ret)
