# 凸包 Monotone Chain O(nlogn)
# 参考: https://matsu7874.hatenablog.com/entry/2018/12/17/025713
def get_convex_hull(points):
    def det(p, q):
        return p[0] * q[1] - p[1] * q[0]
    def sub(p, q):
        return (p[0] - q[0], p[1] - q[1])
    points.sort()
    ch = []
    for p in points:
        while len(ch) > 1:
            v_cur = sub(ch[-1], ch[-2])
            v_new = sub(p, ch[-2])
            if det(v_cur, v_new) > 0:
                break
            ch.pop()
        ch.append(p)
    t = len(ch)
    for p in points[-2::-1]:
        while len(ch) > t:
            v_cur = sub(ch[-1], ch[-2])
            v_new = sub(p, ch[-2])
            if det(v_cur, v_new) > 0:
                break
            ch.pop()
        ch.append(p)
    return ch[:-1]
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
ps = [(0, 0)]
for x, y in XY:
    ps_new = ps[:]
    for x_, y_ in ps:
        ps_new.append((x+x_, y+y_))
    ps = get_convex_hull(ps_new)
ans = 0
for x, y in ps:
    ans = max(ans, x*x+y*y)
print(ans ** 0.5)
