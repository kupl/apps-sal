(n, t) = list(map(int, input().split()))
total = sum(range(1, n + 1))
l = [[0] * i for i in range(1, n + 1)]
max_d = sum(range(1, n + 1))
d = 0


def f(l, lvl, i, inc):
    if lvl >= len(l) or i >= len(l[lvl]):
        return
    if l[lvl][i] < 1:
        tmp = l[lvl][i] + inc
        if tmp > 1:
            inc = tmp - 1
            l[lvl][i] = 1
        else:
            l[lvl][i] += inc
            inc = 0
    if inc == 0:
        return
    inc /= 2
    lvl += 1
    f(l, lvl, i, inc)
    f(l, lvl, i + 1, inc)


def count(l):
    ans = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] >= 1:
                ans += 1
    return ans


f(l, 0, 0, t)
print(count(l))
