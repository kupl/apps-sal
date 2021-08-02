def answer(H, W, ans):

    for x in range(1, W):
        y1 = H // 2
        Sa1 = H * x
        Sb1 = (W - x) * y1
        Sc1 = (W - x) * (H - y1)
        M = max(Sa1, Sb1, Sc1)
        m = min(Sa1, Sb1, Sc1)

        y2 = (W - x) // 2
        Sa2 = H * x
        Sb2 = H * y2
        Sc2 = H * (W - x - y2)
        M2 = max(Sa2, Sb2, Sc2)
        m2 = min(Sa2, Sb2, Sc2)

        if ans > min(M - m, M2 - m2):
            ans = min(M - m, M2 - m2)

    return ans


def __starting_point():
    H, W = [int(i) for i in input().split()]
    ans = H * W
    ans = answer(H, W, ans)

    H, W = W, H

    if answer(H, W, ans) < ans:
        ans = answer(H, W, ans)

    print(ans)


__starting_point()
