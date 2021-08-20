import collections
(h, w) = map(int, input().split())


def hkara(h, w):
    hans = 10 ** 9
    for i in range(1, h):
        fst = w * i
        snd = w // 2 * (h - i)
        trd = (w - w // 2) * (h - i)
        mx = max(max(fst, snd), trd)
        mn = min(min(fst, snd), trd)
        hans = min(mx - mn, hans)
        tfst = w * i
        tsnd = (h - i) // 2 * w
        ttrd = (h - (h - i) // 2 - i) * w
        tmx = max(max(tfst, tsnd), ttrd)
        tmn = min(min(tfst, tsnd), ttrd)
        hans = min(tmx - tmn, hans)
    return hans


def wkara(h, w):
    wans = 10 ** 9
    for i in range(1, w):
        fst = h * i
        snd = h // 2 * (w - i)
        trd = (h - h // 2) * (w - i)
        mx = max(max(fst, snd), trd)
        mn = min(min(fst, snd), trd)
        wans = min(mx - mn, wans)
        tfst = h * i
        tsnd = (w - i) // 2 * h
        ttrd = (w - (w - i) // 2 - i) * h
        tmx = max(max(tfst, tsnd), ttrd)
        tmn = min(min(tfst, tsnd), ttrd)
        wans = min(tmx - tmn, wans)
    return wans


print(min(hkara(h, w), wkara(h, w)))
