n, m = [int(x) for x in input().split()]
L = [[int(x) for x in input().split()] for z in range(m)]
maxh = max([x[1] for x in L])


def possible(a, b):
    if abs(a[1] - b[1]) > abs(a[0] - b[0]):
        return False
    return True


def maxp(a, b):
    t = abs(a[0] - b[0])
    t -= abs(a[1] - b[1])
    m = max(a[1], b[1])
    return m + (t // 2)


poss = True
for i in range(len(L) - 1):
    if not possible(L[i], L[i + 1]):
        poss = False
        break
    maxh = max(maxh, maxp(L[i], L[i + 1]))
maxh = max(maxh, L[0][0] - 1 + L[0][1], n - L[-1][0] + L[-1][1])
if poss:
    print(maxh)
else:
    print('IMPOSSIBLE')
