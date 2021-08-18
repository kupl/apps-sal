
def get_convex_hull(points):
    def det(p, q):
        return (p.conjugate() * q).imag
    points.sort(key=lambda x: (x.real, x.imag))
    ch = []
    for p in points:
        while len(ch) > 1:
            v_cur = ch[-1] - ch[-2]
            v_new = p - ch[-2]
            if det(v_cur, v_new) > 0:
                break
            ch.pop()
        ch.append(p)
    t = len(ch)
    for p in points[-2::-1]:
        while len(ch) > t:
            v_cur = ch[-1] - ch[-2]
            v_new = p - ch[-2]
            if det(v_cur, v_new) > 0:
                break
            ch.pop()
        ch.append(p)
    return ch[:-1]


N = int(input())
XY = [complex(*list(map(int, input().split()))) for _ in range(N)]
ps = [complex(0, 0)]
for p in XY:
    ps_new = ps[:]
    for p_ in ps:
        ps_new.append(p + p_)
    ps = get_convex_hull(ps_new)
ans = 0
for p in ps:
    ans = max(ans, abs(p))
print(ans)
