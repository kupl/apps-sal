(s, b) = list(map(int, input().split()))
spaceships = list(map(int, input().split()))
bases = [tuple(map(int, input().split())) for i in range(b)]
bases.sort()
sumbases = [bases[i][1] for i in range(b)]
for i in range(1, b):
    sumbases[i] += sumbases[i - 1]


def search_bases(strength):
    (l, r) = (0, b)
    while l < r:
        m = (l + r) // 2
        if bases[m][0] <= strength:
            l = m + 1
        else:
            r = m
    return l - 1


def res(x):
    i = search_bases(x)
    if i < 0:
        return 0
    else:
        return sumbases[i]


print(*tuple(map(res, spaceships)))
