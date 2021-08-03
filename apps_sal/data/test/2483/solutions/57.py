from itertools import accumulate


def main():
    n, c = list(map(int, input().split()))
    p = [[] for _ in range(c + 1)]
    for _ in range(n):
        *st, cc = list(map(int, input().split()))
        p[cc].append(st)
    all_p = [0] * (10 ** 5 + 10)
    for pp in p:
        if len(pp) == 0:
            continue
        pp.sort()
        last_start, last_end = pp[0]
        for start, end in pp[1:]:
            if start == last_end:
                last_end = end
            else:
                all_p[last_start - 1] += 1
                all_p[last_end] -= 1
                last_start, last_end = start, end
        all_p[last_start - 1] += 1
        all_p[last_end] -= 1
    print((max(accumulate(all_p))))


def __starting_point():
    main()


__starting_point()
