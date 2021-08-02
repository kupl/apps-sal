from bisect import bisect_left
# 初期入力
import sys
input = sys.stdin.readline  # 文字列では使わない
A, B, Q = (int(i) for i in input().split())
st = {"s": [], "t": []}
x = [0] * Q

for i in range(A):
    aa = int(input())
    st["s"].append(aa)
st["s"].append(10**11)

for i in range(B):
    bb = int(input())
    st["t"].append(bb)
st["t"].append(10**11)


for i in range(Q):
    x[i] = int(input())

# 2分探索で近い神社と寺を探す
dist = []
for xi in x:
    # スタート⇒神社
    xs = bisect_left(st["s"], xi)
    s_l = st["s"][xs - 1]  # スタート地点から近い神社（左）⓵
    s_r = st["s"][xs]  # スタート地点から近い神社（右）⓶
    xs_l = abs(xi - s_l)
    xs_r = abs(xi - s_r)

    xs_l_t = bisect_left(st["t"], s_l)
    t_l = st["t"][xs_l_t - 1]  # ⓵から近い寺（左）
    t_r = st["t"][xs_l_t]  # ⓵から近い寺（右）
    xs_l_t_l = abs(s_l - t_l)
    xs_l_t_r = abs(s_l - t_r)

    xs_r_t = bisect_left(st["t"], s_r)
    t_l = st["t"][xs_r_t - 1]  # ⓶から近い寺（左）
    t_r = st["t"][xs_r_t]  # ⓶から近い寺（右）
    xs_r_t_l = abs(s_r - t_l)
    xs_r_t_r = abs(s_r - t_r)
    ds = min(xs_l + xs_l_t_l, xs_l + xs_l_t_r, xs_r + xs_r_t_l, xs_r + xs_r_t_r)

    # スタート⇒寺
    xs = bisect_left(st["t"], xi)
    s_l = st["t"][xs - 1]  # スタート地点から近い寺（左）⓷
    s_r = st["t"][xs]  # スタート地点から近い寺（右）⓸
    xs_l = abs(xi - s_l)
    xs_r = abs(xi - s_r)

    xs_l_t = bisect_left(st["s"], s_l)
    t_l = st["s"][xs_l_t - 1]  # ⓷から近い神社（左）
    t_r = st["s"][xs_l_t]  # ⓷から近い神社（右）
    xs_l_t_l = abs(s_l - t_l)
    xs_l_t_r = abs(s_l - t_r)

    xs_r_t = bisect_left(st["s"], s_r)
    t_l = st["s"][xs_r_t - 1]  # ⓸から近い神社（左）
    t_r = st["s"][xs_r_t]  # ⓸から近い神社（右）
    xs_r_t_l = abs(s_r - t_l)
    xs_r_t_r = abs(s_r - t_r)
    dt = min(xs_l + xs_l_t_l, xs_l + xs_l_t_r, xs_r + xs_r_t_l, xs_r + xs_r_t_r)
    print((min(ds, dt)))
