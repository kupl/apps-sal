from itertools import permutations
from bisect import bisect_left


def main():
    inf = float("inf")
    n, m = map(int, input().split())
    weight = sorted(list(map(int, input().split())))
    bridge = [tuple(map(int, input().split())) for _ in range(m)]

    bridge.sort(key=lambda x: x[1])
    bridge_w = [x[1] for x in bridge]
    bridge_l = [0] * (m + 1)
    for i in range(m):
        bridge_l[i + 1] = max(bridge[i][0], bridge_l[i])

    if weight[-1] > bridge_w[0]:
        print(-1)
        return

    mn = inf
    for x in permutations(weight):
        dis = [[0] * n for _ in range(n)]

        for i in range(1, n):
            for j in range(n - i):
                work_weight = sum(x[j:j + i + 1])
                work_index = bisect_left(bridge_w, work_weight)
                mx = bridge_l[work_index]
                for l in range(1, i):
                    if dis[j][j + l] + dis[j + l][j + i] > mx:
                        mx = dis[j][j + l] + dis[j + l][j + i]
                dis[j][j + i] = mx
        if dis[0][n - 1] < mn:
            mn = dis[0][n - 1]

    print(mn)


main()
