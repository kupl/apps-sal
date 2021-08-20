def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


(x0, y0, a1, a2, b1, b2) = list(map(int, input().split()))
(xs, ys, t) = list(map(int, input().split()))
arr = []
arr.append((x0, y0))
now1 = x0
now2 = y0
while 1:
    now1 = a1 * now1 + b1
    now2 = a2 * now2 + b2
    if now1 < xs or now2 < ys:
        arr.append((now1, now2))
        continue
    arr.append((now1, now2))
    if dist(now1, now2, xs, ys) > t:
        break
ans = 0
N = len(arr)
for i in range(N):
    need = dist(arr[i][0], arr[i][1], xs, ys)
    if need > t:
        continue
    left = t - need
    now = 1
    flag = 1
    now1 = arr[i][0]
    now2 = arr[i][1]
    for j in range(i - 1, -1, -1):
        d = dist(now1, now2, arr[j][0], arr[j][1])
        if d > left:
            flag = 0
            break
        left -= d
        now1 = arr[j][0]
        now2 = arr[j][1]
        now += 1
    if not flag:
        ans = max(ans, now)
        continue
    for j in range(i + 1, N):
        d = dist(now1, now2, arr[j][0], arr[j][1])
        if d > left:
            break
        left -= d
        now1 = arr[j][0]
        now2 = arr[j][1]
        now += 1
    ans = max(ans, now)
print(ans)
