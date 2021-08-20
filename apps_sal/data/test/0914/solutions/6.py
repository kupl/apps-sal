from collections import Counter
from heapq import heappushpop


def main():
    (cnt, n) = (Counter(input()), int(input()))
    if n < len(cnt):
        print(-1)
        return
    h = list(((1 / v, 1, c) for (c, v) in cnt.most_common()))
    res = list(cnt.keys())
    (_, v, c) = h.pop(0)
    for _ in range(n - len(cnt)):
        res.append(c)
        v += 1
        (_, v, c) = heappushpop(h, (v / cnt[c], v, c))
    print((cnt[c] + v - 1) // v)
    print(''.join(res))


def __starting_point():
    main()


__starting_point()
