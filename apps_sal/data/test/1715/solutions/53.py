from bisect import bisect_left
import sys
input = sys.stdin.readline
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

dist = []
for xi in x:
    xs = bisect_left(st["s"], xi)
    s_l = st["s"][xs - 1]
    s_r = st["s"][xs]
    xs_l = abs(xi - s_l)
    xs_r = abs(xi - s_r)

    xs_l_t = bisect_left(st["t"], s_l)
    t_l = st["t"][xs_l_t - 1]
    t_r = st["t"][xs_l_t]
    xs_l_t_l = abs(s_l - t_l)
    xs_l_t_r = abs(s_l - t_r)

    xs_r_t = bisect_left(st["t"], s_r)
    t_l = st["t"][xs_r_t - 1]
    t_r = st["t"][xs_r_t]
    xs_r_t_l = abs(s_r - t_l)
    xs_r_t_r = abs(s_r - t_r)
    ds = min(xs_l + xs_l_t_l, xs_l + xs_l_t_r, xs_r + xs_r_t_l, xs_r + xs_r_t_r)

    xs = bisect_left(st["t"], xi)
    s_l = st["t"][xs - 1]
    s_r = st["t"][xs]
    xs_l = abs(xi - s_l)
    xs_r = abs(xi - s_r)

    xs_l_t = bisect_left(st["s"], s_l)
    t_l = st["s"][xs_l_t - 1]
    t_r = st["s"][xs_l_t]
    xs_l_t_l = abs(s_l - t_l)
    xs_l_t_r = abs(s_l - t_r)

    xs_r_t = bisect_left(st["s"], s_r)
    t_l = st["s"][xs_r_t - 1]
    t_r = st["s"][xs_r_t]
    xs_r_t_l = abs(s_r - t_l)
    xs_r_t_r = abs(s_r - t_r)
    dt = min(xs_l + xs_l_t_l, xs_l + xs_l_t_r, xs_r + xs_r_t_l, xs_r + xs_r_t_r)
    print((min(ds, dt)))
