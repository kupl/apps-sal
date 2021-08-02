from math import ceil


def main():
    H, W = list(map(int, input().split()))
    if H * W % 3 == 0:
        print((0))
        return
    ans1 = float('inf')
    ans2 = float('inf')
    ans3 = min(H, W)
    # h == Tの上
    for h in range(1, H + 1):
        if W % 2 == 0:
            ans1 = min(ans1, abs(h * (W // 2) - W * (H - h)))
        else:
            ans1 = min(
                ans1,
                max([
                    abs((h * (W // 2) - W * (H - h))),
                    abs(h * ((W + 1) // 2) - W * (H - h)),
                    h
                ]))
    for w in range(1, W + 1):
        if H % 2 == 0:
            ans2 = min(ans2, abs(w * (H // 2) - H * (W - w)))
        else:
            ans2 = min(
                ans2, max([abs((w * (H // 2) - H * (W - w))), abs(w * ((H + 1) // 2) - H * (W - w)), w]))
    print((min([ans1, ans2, ans3])))
    return


def __starting_point():
    main()


__starting_point()
