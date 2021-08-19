from itertools import permutations


def f(perm):
    res = 0
    for i in range(len(perm)):
        for j in range(i, len(perm)):
            res += min(perm[i:j + 1])
    return res


(n, m) = list(map(int, input().split()))
res = f(list(range(1, n + 1)))
i = 0
for p in permutations(list(range(1, n + 1))):
    if f(p) == res:
        i += 1
        if i == m:
            print(' '.join(list(map(str, p))))
            break
