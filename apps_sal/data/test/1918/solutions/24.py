def main():
    input()
    pp = list(map(int, input().split()))
    mask = [c == 'B' for c in input()]
    s = t = sum(p for p, m in zip(pp, mask) if m)
    res = [s]
    for p, m in zip(pp, mask):
        if m:
            s -= p
        else:
            s += p
            res.append(s)
    pp.reverse()
    mask.reverse()
    for p, m in zip(pp, mask):
        if m:
            t -= p
        else:
            t += p
            res.append(t)
    print(max(res))


def __starting_point():
    main()

__starting_point()
