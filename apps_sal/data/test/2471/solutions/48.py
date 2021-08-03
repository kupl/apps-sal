from collections import deque, defaultdict, Counter
import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15


def main():
    H, W, N = map(int, input().split())
    point = [tuple(map(int, input().split())) for _ in range(N)]
    ans = [0] * 10

    dic = defaultdict(int)
    for p, q in point:
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if p + dy <= 1 or p + dy >= H:
                    continue
                if q + dx <= 1 or q + dx >= W:
                    continue
                center = (p + dy, q + dx)
                ans[dic[center]] -= 1
                dic[center] += 1
                ans[dic[center]] += 1
    ans[0] += (H - 2) * (W - 2)
    print('\n'.join(map(str, ans)))


def __starting_point():
    main()


__starting_point()
