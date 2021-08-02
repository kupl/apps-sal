import sys
from itertools import combinations
input = sys.stdin.readline


def main():
    h, w, n = list(map(int, input().split()))
    grid = [0] * n
    mod = 10**9
    judge = dict()
    for _ in range(n):
        a, b = list(map(int, input().split()))
        for i in range(-1, 2):
            for j in range(-1, 2):
                if a + i <= 1 or a + i >= h or b + j <= 1 or b + j >= w:
                    continue
                if (a + i, b + j) in judge:
                    judge[(a + i, b + j)] += 1
                else:
                    judge[(a + i, b + j)] = 1

    ans = [0] * 10

    for v in list(judge.values()):
        ans[v] += 1
    ans[0] = (h - 2) * (w - 2) - sum(ans[1:])

    for a in ans:
        print(a)


def __starting_point():
    main()


__starting_point()
