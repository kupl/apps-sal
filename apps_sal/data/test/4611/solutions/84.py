cnt = int(input())
(t_s, x_s, y_s) = (0, 0, 0)
for _ in range(cnt):
    (t, x, y) = map(int, input().split())
    (d_t, d_x, d_y) = (t - t_s, x - x_s, y - y_s)
    z = abs(d_x + d_y)
    if z > d_t or (d_t - z) % 2 == 1:
        print('No')
        break
    (t_s, x_s, y_s) = (t, x, y)
else:
    print('Yes')
