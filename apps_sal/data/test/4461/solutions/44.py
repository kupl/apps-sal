(h, w) = list(map(int, input().split()))


def defs(h, w):
    ans = 10 ** 12
    for i in range(1, h):
        sa = i * w
        h2 = h - i
        for j in range(2):
            if j == 0:
                sb = h2 * (w // 2)
                sc = h2 * (w - w // 2)
            else:
                sb = h2 // 2 * w
                sc = (h - i - h2 // 2) * w
            s_max = max(sa, sb, sc)
            s_min = min(sa, sb, sc)
            ans = min(ans, s_max - s_min)
    return ans


print(min(defs(h, w), defs(w, h)))
