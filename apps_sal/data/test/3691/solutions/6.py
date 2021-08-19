(x0, y0, ax, ay, bx, by) = list(map(int, input().split()))
(xs, ys, t) = list(map(int, input().split()))
x = [x0]
y = [y0]
while x[-1] < xs or y[-1] < ys or abs(x[-1] - xs) + abs(y[-1] - ys) <= 2 * t:
    x.append(x[-1] * ax + bx)
    y.append(y[-1] * ay + by)
x.append(x[-1] * ax + bx)
y.append(y[-1] * ay + by)
ans = 0
for i in range(len(x)):
    cur_t = 0
    cnt = 0
    cur_x = xs
    cur_y = ys
    for j in range(i, -1, -1):
        if cur_t + abs(cur_x - x[j]) + abs(cur_y - y[j]) <= t:
            cnt += 1
            cur_t += abs(cur_x - x[j]) + abs(cur_y - y[j])
            cur_x = x[j]
            cur_y = y[j]
    for j in range(i + 1, len(x)):
        if cur_t + abs(cur_x - x[j]) + abs(cur_y - y[j]) <= t:
            cnt += 1
            cur_t += abs(cur_x - x[j]) + abs(cur_y - y[j])
            cur_x = x[j]
            cur_y = y[j]
    ans = max(cnt, ans)
print(ans)
