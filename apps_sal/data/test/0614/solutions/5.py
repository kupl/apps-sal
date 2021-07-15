def f():
    n, m = list(map(int, input().split()))
    l = list(tuple(map(int, input().split())) for _ in range(n))
    l.sort(key=lambda e: (0, 6, 3, 2)[e[0]] * e[1], reverse=True)
    last, r = [0] * 4, 0
    for i, (w, c) in enumerate(l):
        if m < w:
            break
        m -= w
        r += c
        last[w] = c
    else:
        return r
    if not m:
        return r
    res, tail = [r], (None, [], [], [])
    for w, c in l[i:]:
        tail[w].append(c)
    for w in 1, 2, 3:
        tail[w].append(0)
    _, t1, t2, t3 = tail
    if m == 1:
        res.append(r + t1[0])
        if last[1]:
            res.append(r - last[1] + t2[0])
        if last[2]:
            res.append(r - last[2] + t3[0])
        if last[3]:
            r -= last[3]
            res += (r + sum(t1[:4]), r + sum(t1[:2]) + t2[0], r + sum(t2[:2]))
    else:  # m == 2
        res += (r + sum(t1[:2]), r + t2[0])
        if last[1]:
            res.append(r - last[1] + t3[0])
        if last[2]:
            res.append(r - last[2] + t3[0] + t1[0])
    return max(res)


def main():
    print(f())


def __starting_point():
    main()

__starting_point()
