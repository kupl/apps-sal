from bisect import bisect_right, bisect_left


def main():
    (n, k, d) = list(map(int, input().split()))
    sat = [int(x) for x in input().split()]
    sat = sorted(sat)
    arrange = [True] + [False for _ in range(n)]
    s = 0
    i = min(bisect_right(sat, sat[s] + d), k)
    n_arrange = 1 if s <= i - k else 0
    while i <= n:
        if i - s >= k and n_arrange > 0:
            arrange[i] = True
        if i < n:
            news = bisect_left(sat, sat[i] - d, s, i)
            while s < news:
                if s <= i - k and arrange[s]:
                    n_arrange -= 1
                s += 1
        i += 1
        n_arrange += 1 if s <= i - k and arrange[i - k] else 0
    if arrange[n]:
        print('YES')
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
