import itertools
import math


def main():
    N = int(input())
    coords = [list(map(int, input().split(' '))) for _ in range(N)]
    ans_squared = 10 ** 12
    # 2点を通る円で、全点覆える円の半径の最小値を求める
    for i, j in itertools.combinations(range(N), 2):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        d_squared = (x1 - x2)**2 + (y1 - y2)**2
        cover = True
        for n in range(N):
            x, y = coords[n]
            if (2 * x - (x1 + x2))**2 + (2 * y - (y1 + y2))**2 > d_squared:
                cover = False
                break
        if cover:
            ans_squared = min(ans_squared, d_squared / 4)
    if N == 2:
        print(math.sqrt(ans_squared))
        return
    # 3点を通る円で、全点覆える円の半径の最小値を求める
    for i, j, k in itertools.combinations(range(N), 3):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        x3, y3 = coords[k]
        dx12, dx23, dy12, dy23 = x1 - x2, x2 - x3, y1 - y2, y2 - y3
        if dx12 * dy23 == dy12 * dx23:
            # 3点が1直線上にのってると、3点を通る円が描けない
            continue
        v1, v2, v3 = x1 ** 2 + y1 ** 2, x2 ** 2 + y2 ** 2, x3 ** 2 + y3 ** 2
        scale = 2 * (dx12 * dy23 - dy12 * dx23)
        # 中心座標（のscale倍）
        scaled_cx = dy23 * v1 - (dy12 + dy23) * v2 + dy12 * v3
        scaled_cy = - dx23 * v1 + (dx12 + dx23) * v2 - dx12 * v3
        r_squared = (x1 - scaled_cx / scale)**2 + (y1 - scaled_cy / scale)**2
        cover = True
        for n in range(N):
            x, y = coords[n]
            if (scale * x - scaled_cx)**2 + (scale * y - scaled_cy)**2 \
                    > (scale * x1 - scaled_cx)**2 + (scale * y1 - scaled_cy)**2:
                cover = False
        if cover:
            ans_squared = min(ans_squared, r_squared)
    print(math.sqrt(ans_squared))


def __starting_point():
    main()


__starting_point()
