from itertools import product
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    (h, w, k) = map(int, input().split())
    C = [input() for _ in range(h)]
    comb_list = list(product([False, True], repeat=h + w))
    ans = 0
    for comb in comb_list:
        cunt = 0
        for i in range(h):
            if not comb[i]:
                continue
            for j in range(w):
                if not comb[h + j]:
                    continue
                if C[i][j] == '#':
                    cunt += 1
        if cunt == k:
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
