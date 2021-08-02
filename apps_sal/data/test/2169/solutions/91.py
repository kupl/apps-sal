def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)

    from collections import defaultdict
    from itertools import accumulate

    h, w, d = list(map(int, readline().split()))
    dict = defaultdict(list)
    memo = [[0] for _ in range(d + 1)]
    for i in range(h):
        a = list(map(int, readline().split()))
        for j, aa in enumerate(a):
            dict[aa] = [i, j]
    for i in range(1, d + 1):
        bf = i
        for af in range(i + d, h * w + 1, d):
            memo[i].append(abs(dict[bf][0] - dict[af][0]) + abs(dict[bf][1] - dict[af][1]))
            bf = af
        memo[i] = list(accumulate(memo[i]))
    q = int(readline())
    for _ in range(q):
        l, r = list(map(int, readline().split()))
        if r < l:
            r, l = l, r
        l, i = divmod(l, d)
        r //= d
        if i == 0:
            i = d
            l -= 1
            r -= 1
        print((memo[i][r] - memo[i][l]))


def __starting_point():
    main()


__starting_point()
