from itertools import combinations


def main():
    N, K = list(map(int, input().split()))
    P = [list(map(int, input().split())) for _ in range(N)]
    ans = 1 << 62
    for t in combinations(P, min(4, K)):
        xs, ys = list(zip(*t))
        xmin = min(xs)
        xmax = max(xs)
        ymin = min(ys)
        ymax = max(ys)
        area = (xmax - xmin) * (ymax - ymin)
        if ans < area:
            continue
        k = 0
        for x, y in P:
            if xmin <= x <= xmax and ymin <= y <= ymax:
                k += 1
        if k >= K:
            ans = area
    print(ans)


main()
