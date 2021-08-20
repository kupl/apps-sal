import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    (H, W, n) = map(int, input().split())
    AB = set(tuple((tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n))))
    d = ((1, 1), (1, 0), (1, -1), (0, 1), (0, 0), (0, -1), (-1, 1), (-1, 0), (-1, -1))
    target = set()
    res = [0] * 10
    for (h, w) in AB:
        cnt = 0
        flg = True
        for (dh, dw) in d:
            (next_h, next_w) = (h + dh, w + dw)
            if next_h < 0 or next_h >= H or next_w < 0 or (next_w >= W):
                flg = False
            if (next_h, next_w) in AB:
                cnt += 1
            else:
                target.add((next_h, next_w))
        if flg:
            res[cnt] += 1
    for (h, w) in target:
        cnt = 0
        for (dh, dw) in d:
            (next_h, next_w) = (h + dh, w + dw)
            if next_h < 0 or next_h >= H or next_w < 0 or (next_w >= W):
                break
            if (next_h, next_w) in AB:
                cnt += 1
        else:
            res[cnt] += 1
    total = (H - 2) * (W - 2)
    res[0] = total - sum(res)
    print(*res, sep='\n')


def __starting_point():
    resolve()


__starting_point()
