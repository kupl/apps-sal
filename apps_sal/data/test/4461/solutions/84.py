import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = list(map(int, input().split()))

    if H % 3 == 0 or W % 3 == 0:
        print((0))
        return

    res = f_inf
    for h in range(H):
        A = h * W

        B = W * ((H - h) // 2)
        C = W * ((H - h) - (H - h) // 2)
        ma = max(A, B, C)
        mi = min(A, B, C)
        res = min(res, ma - mi)

        B = (H - h) * (W // 2)
        C = (H - h) * (W - W // 2)
        ma = max(A, B, C)
        mi = min(A, B, C)
        res = min(res, ma - mi)

    for w in range(W):
        A = w * H

        B = H * ((W - w) // 2)
        C = H * ((W - w) - (W - w) // 2)
        ma = max(A, B, C)
        mi = min(A, B, C)
        res = min(res, ma - mi)

        B = (W - w) * (H // 2)
        C = (W - w) * (H - H // 2)
        ma = max(A, B, C)
        mi = min(A, B, C)
        res = min(res, ma - mi)

    print(res)


def __starting_point():
    resolve()

__starting_point()
