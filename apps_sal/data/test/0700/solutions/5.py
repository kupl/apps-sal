from itertools import chain, combinations, permutations


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    return chain.from_iterable((combinations(xs, n) for n in range(len(xs) + 1)))


n = int(input())
cl1 = []
cl2 = []
for i in range(n):
    s = input()
    a = []
    for j in range(n):
        a.append(s[j])
    cl1.append(a)
for i in range(n):
    s = input()
    a = []
    for j in range(n):
        a.append(s[j])
    cl2.append(a)


def copy(m):
    res = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(m[i][j])
        res.append(a)
    return res


def pow(m):
    res = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(m[n - 1 - j][i])
        res.append(a)
    return res


def vert(m):
    res = []
    for i in range(n):
        res.append(m[i][::-1])
    return res


def gor(m):
    res = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(m[i][n - 1 - j])
        res.append(a)
    return res


comblist = [[1], []]
cm = [pow, pow, pow, vert, gor]
cm = list(powerset(cm))
res = False
if cl1 == cl2:
    res = True
else:
    for x in cm:
        for y in permutations(x):
            t = copy(cl1)
            for z in y:
                t = z(t)
            if t == cl2:
                res = True
if res:
    print('Yes')
else:
    print('No')
