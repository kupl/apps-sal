from itertools import permutations


def f(l):
    n = len(l)
    res = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            res += min(l[i:j])
    return res


(n, m) = (int(x) for x in input().split())
res = 0
resl = []
for perm in permutations(list(range(1, n + 1))):
    cur = f(perm)
    if cur > res:
        res = cur
        resl = []
    if cur == res:
        resl.append(perm)
print(' '.join((str(x) for x in resl[m - 1])))
