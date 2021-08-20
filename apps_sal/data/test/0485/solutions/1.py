n = int(input())
l = [list(map(int, input().split())) for _ in range(4 * n + 1)]
(x, y) = list(map(list, list(zip(*l))))
(hx, lx, hy, ly) = (max(x), min(x), max(y), min(y))


def find(w, i):
    for j in l:
        if j[w] == i:
            return j


if x.count(hx) == 1:
    print(*find(0, hx))
elif x.count(lx) == 1:
    print(*find(0, lx))
elif y.count(hy) == 1:
    print(*find(1, hy))
elif y.count(ly) == 1:
    print(*find(1, ly))
else:
    for i in l:
        if i[0] not in [hx, lx] and i[1] not in [hy, ly]:
            print(*i)
            break
