import sys
from itertools import combinations
from math import atan2, cos, sin


def apollonius(p1, c1, p2, c2):
    m1 = p1 + (p2 - p1) * c2 / (c1 + c2)
    m2 = p1 + (p2 - p1) * c2 / (c2 - c1)
    m = (m1 + m2) / 2
    r = abs(m1 - m)
    return m, r


def apollonius_intersections(p1, c1, p2, c2, p3, c3):
    m12, r12 = apollonius(p1, c1, p2, c2)
    m13, r13 = apollonius(p1, c1, p3, c3)
    v = m13 - m12
    d = abs(v)
    if d > r12 + r13 or d < abs(r12 - r13):
        return None, None
    theta = atan2(v.imag, v.real)
    xx = (r12 ** 2 - r13 ** 2 + d ** 2) / (2 * d)
    s = (r12 + r13 + d) / 2
    yy = 2 * (s * (s - r12) * (s - r13) * (s - d)) ** 0.5 / d
    st = sin(theta)
    ct = cos(theta)
    e1 = (xx * ct - yy * st) + (xx * st + yy * ct) * 1j + m12
    e2 = (xx * ct + yy * st) + (xx * st - yy * ct) * 1j + m12

    t1 = abs(e1 - p1) * c1
    t2 = abs(e2 - p1) * c1
    if t1 < t2:
        return e1, t1
    return e2, t2


def get_circumscribed_center(p1, p2, p3):
    A = abs(p2 - p3) ** 2
    B = abs(p3 - p1) ** 2
    C = abs(p1 - p2) ** 2
    T = A * (B + C - A)
    U = B * (C + A - B)
    W = C * (A + B - C)
    try:
        return (T * p1 + U * p2 + W * p3) / (T + U + W)
    except:
        return 0j


def solve(n, k, xyc):
    if k == 1:
        return 0

    xxx = xyc[0::3]
    yyy = xyc[1::3]
    ccc = xyc[2::3]
    beefs = [(i, x + y * 1j, c) for i, (x, y, c) in enumerate(zip(xxx, yyy, ccc))]

    ans = 1e18
    for (i1, p1, c1), (i2, p2, c2) in combinations(beefs, 2):
        # 肉2枚の比重を考慮した等距離点に熱源を置いたときの時間tを算出
        # →t以内に焼ける肉がK以上あれば、その2枚を含む場合の最小時間はt
        px = p1 + (p2 - p1) * (c2 / (c1 + c2))
        t = abs(px - p1) * c1 + 1e-8

        ok = 0
        ng = []
        for i, p, c in beefs:
            if abs(px - p) * c <= t:
                ok += 1
            else:
                ng.append(i)
        if ok >= k:
            ans = min(ans, t)
            continue
        # p1,p2の2点を含む場合の時間は、これ以上小さくならない
        if ans <= t:
            continue

        # K枚以上ない場合、範囲外のどれかの肉をギリギリ含めることを考える
        # （重複を防ぐため、j > i2 の肉を調べる）
        # 2点からの比が等しい点の軌跡は、c1==c2なら垂直二等分線、それ以外はアポロニウスの円
        # p1-p2, p2-p3, p3-p1 の3円（または直線）が1点で交わる箇所があるか
        # ある → そこに熱源を置き、時間tを算出、t以内に焼ける肉がK以上あるか調べる
        # ない → 他の2点または3点で考えた方がよい
        for i3 in ng:
            if i3 < i2:
                continue
            _, p3, c3 = beefs[i3]
            if c1 == c2:
                if c2 == c3:
                    e = get_circumscribed_center(p1, p2, p3)
                    t = abs(e - p1) * c1
                else:
                    e, t = apollonius_intersections(p3, c3, p1, c1, p2, c2)
            elif c1 == c3:
                e, t = apollonius_intersections(p2, c2, p1, c1, p3, c3)
            else:
                e, t = apollonius_intersections(p1, c1, p2, c2, p3, c3)

            if e is None:
                continue

            t += 1e-8
            ok2 = 0
            for i, p, c in beefs:
                if abs(e - p) * c <= t:
                    ok2 += 1
            if ok2 >= k:
                ans = min(ans, t)

    return ans


n, k = list(map(int, input().split()))
xyc = list(map(int, sys.stdin.read().split()))
print((solve(n, k, xyc)))

