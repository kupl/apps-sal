from bisect import bisect_right, bisect_left


def main():
    n, k, d = map(int, input().split())
    sat = [int(x) for x in input().split()]

    sat = sorted(sat)
    arrange = [False for _ in range(n + 1)]
    arrange[0] = True
    s = 0
    # i means the first i items could be arranged well
    i = min(bisect_right(sat, sat[s] + d), k)
    n_arrange = 1 if i - k >= 0 else 0 # arrange[0] == True | the first 0 items

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
        n_arrange += 1 if (i - k >= s and arrange[i - k]) else 0

    if arrange[n]:
        print('YES')
    else:
        print('NO')


def __starting_point():
    main()
__starting_point()
