import sys


def func(op, val):
    target = []
    for (i, o) in enumerate(op):
        if sum([val[k] for k in o]) == 0:
            return []
        k0 = o[0]
        k1 = o[1]
        if val[k0] == 0:
            (p, m) = (k0, k1)
        elif val[k1] == 0:
            (p, m) = (k1, k0)
        elif i < len(op) - 1 and k1 in op[i + 1]:
            (p, m) = (k1, k0)
        else:
            (p, m) = (k0, k1)
        val[p] += 1
        val[m] -= 1
        target.append(p)
    return target


(n, a, b, c) = [int(x) for x in input().split()]
operation = [sys.stdin.readline().strip() for _ in range(n)]
val = {'A': a, 'B': b, 'C': c}
target = func(operation, val)
if len(target) == 0:
    print('No')
else:
    print('Yes')
    for t in target:
        print(t)
