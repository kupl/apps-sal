import sys
readline = sys.stdin.readline


def main():
    H, W = map(int, readline().rstrip().split())
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    res = [[-1] * W for _ in range(H)]
    ht, wt = 0, 0
    for i, a in enumerate(A):
        while a:
            res[ht][wt] = i + 1
            a -= 1
            if (ht % 2 == 0 and wt == W - 1) or (ht % 2 == 1 and wt == 0):
                ht += 1
            elif ht % 2 == 0:
                wt += 1
            else:
                wt -= 1

    for l in res:
        print(*l, sep=' ')


def __starting_point():
    main()


__starting_point()
