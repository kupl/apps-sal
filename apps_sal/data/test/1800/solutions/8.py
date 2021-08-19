def main():
    from collections import deque
    (n, m) = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    l = list((tuple(map(int, input().split())) for _ in range(m)))
    (tmp, r0, t0) = ([(0, 0)], 0, 0)
    for (t, r) in reversed(l):
        if r0 < r:
            r0 = r
            if t0 != t:
                t0 = t
                tmp.append((t, r))
            else:
                tmp[-1] = (t, r)
    (t0, r0) = tmp.pop()
    q = deque(sorted(aa[:r0]))
    aa = aa[r0:]
    aa.reverse()
    ff = (None, q.pop, q.popleft)
    for (t, r) in reversed(tmp):
        f = ff[t0]
        for i in range(r0 - r):
            aa.append(f())
        (t0, r0) = (t, r)
    print(' '.join(map(str, reversed(aa))))


def __starting_point():
    main()


__starting_point()
