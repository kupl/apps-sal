def main():
    H, W = (int(_) for _ in input().split())
    INF = 10 ** 11

    def calc(h, w):
        # 縦に割る
        w1 = w // 2
        w2 = w - w1
        ret = INF
        for hh in range(1, h):
            ret = min(ret, max(w * hh, (h-hh)*w1, (h-hh)*w2) - min(w * hh, (h-hh)*w1, (h-hh)*w2))
        #横に割る
        for hh in range(1, h):
            h1 = (h-hh)//2
            h2 = h - hh - h1
            ret = min(ret, max(w*hh, w*h1, w*h2) - min(w*hh, w*h1, w*h2))
        return ret
    m1 = calc(H, W)
    m2 = calc(W, H)
    print((min(m1, m2)))
    return
def __starting_point():
    main()

__starting_point()
