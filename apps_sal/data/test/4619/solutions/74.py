w, h, n = map(int, input().split())

x = [0] * n
y = [0] * n
a = [0] * n

for i in range(n):
    x[i], y[i], a[i] = map(int, input().split())

w_l = 0
h_l = 0
for i in range(n):
    if a[i] == 1:
        if w_l < x[i]:
            w_l = x[i]
    elif a[i] == 2:
        if w > x[i]:
            w = x[i]
    elif a[i] == 3:
        if h_l < y[i]:
            h_l = y[i]
    elif a[i] == 4:
        if h > y[i]:
            h = y[i]
W = w - w_l
H = h - h_l
if W < 0 or H < 0:
    ans = 0
else:
    ans = W * H
print(ans)
