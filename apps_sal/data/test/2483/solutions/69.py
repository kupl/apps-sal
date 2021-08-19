import heapq


def main():
    (N, C) = list(map(int, input().split()))
    STC = [tuple(map(int, input().split())) for _ in range(N)]
    STC.sort()
    CC = [(0, 0)] * C
    T = []
    for (s, t, c) in STC:
        (ps, pt) = CC[c - 1]
        if ps == 0:
            CC[c - 1] = (s, t)
        elif s == pt:
            CC[c - 1] = (ps, t)
        else:
            T.append((ps, pt, c))
            CC[c - 1] = (s, t)
    for (c, (s, t)) in enumerate(CC):
        if s != 0:
            T.append((s, t, c + 1))
    T.sort()
    STC = T
    h = []
    e = []
    r = 0
    for (s, t, c) in STC:
        while h and h[0][0] <= s:
            e.append(heapq.heappop(h)[1])
        if not e:
            e.append(r)
            r += 1
        heapq.heappush(h, (t + 1, e.pop()))
    return r


print(main())
