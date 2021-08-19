(w, h, n) = list(map(int, input().split()))
r_w = w
l_w = 0
u_h = h
d_h = 0
for i in range(n):
    (x, y, a) = list(map(int, input().split()))
    if a == 1:
        l_w = max(l_w, x)
    elif a == 2:
        r_w = min(r_w, x)
    elif a == 3:
        d_h = max(d_h, y)
    elif a == 4:
        u_h = min(u_h, y)
res = max(0, r_w - l_w) * max(0, u_h - d_h)
print(res)
