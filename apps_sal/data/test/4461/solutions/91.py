from math import floor, ceil
import sys
readline = sys.stdin.readline


def main():
    H, W = map(int, readline().rstrip().split())
    ans = H * W
    if H >= 3:
        ans = min(ans, abs(W * (H // 3) - W * (H - H // 3 * 2)))
    if W >= 3:
        ans = min(ans, abs(H * (W // 3) - H * (W - W // 3 * 2)))

    x1_cand = [i for i in range(1, W)]
    y1 = H
    for x1 in x1_cand:
        x2 = W - x1
        x3 = x2
        y2 = H // 2
        y3 = H - y2
        ans = min(ans, max((x1 * y1), (x2 * y2), (x3 * y3)) - min((x1 * y1), (x2 * y2), (x3 * y3)))

        x2 = (W - x1) // 2
        x3 = (W - x1 - x2)
        ans = min(ans, max((x1 * H), (x2 * H), (x3 * H)) - min((x1 * H), (x2 * H), (x3 * H)))

    y1_cand = [i for i in range(1, H)]
    x1 = W
    for y1 in y1_cand:
        y2 = H - y1
        y3 = y2
        x2 = W // 2
        x3 = W - x2
        ans = min(ans, max((x1 * y1), (x2 * y2), (x3 * y3)) - min((x1 * y1), (x2 * y2), (x3 * y3)))

        y2 = (H - y1) // 2
        y3 = (H - y1 - y2)
        ans = min(ans, max((W * y1), (W * y2), (W * y3)) - min((W * y1), (W * y2), (W * y3)))

    print(ans)


def __starting_point():
    main()


__starting_point()
