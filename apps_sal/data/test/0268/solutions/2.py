from bisect import bisect_right, bisect_left


def main():
    n, k, d = list(map(int, input().split()))
    sat = [int(x) for x in input().split()]

    sat = sorted(sat)

    # arrange[i] means the first i items could be arranged well
    # arranged well means they could be put into boxes without conflicts
    arrange = [True] + [False for _ in range(n)]

    s = 0

    # we can put [0, i) items into the first box
    i = min(bisect_right(sat, sat[s] + d), k)

    # keep the number of True-value in arrange[s, i-k]
    # there must be at least one point in [s, i-k(included)] which satisfies arrange[this_point] == True
    # that means we can cut from this_point and put [this_point, i) in a new box
    # then the result is arrange[i] become True, because now all items before i-index could be arranged well
    n_arrange = 1 if s <= i - k else 0

    while i <= n:
        if i - s >= k and n_arrange > 0:
            arrange[i] = True
        if i < n:
            # find new s that we could put | item at new s - item at i | <= d
            news = bisect_left(sat, sat[i] - d, s, i)
            while s < news:
                if s <= i - k and arrange[s]:
                    n_arrange -= 1
                s += 1

        i += 1
        # every time when you count arrange[x] you should keep x between [s, i-k]
        n_arrange += 1 if (s <= i - k and arrange[i - k]) else 0

    if arrange[n]:
        print('YES')
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
