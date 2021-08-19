N = int(input())
success = True
(t0, x0, y0) = (0, 0, 0)
for i in range(N):
    (t1, x1, y1) = map(int, input().split())
    dist = abs(x1 - x0) + abs(y1 - y0)
    time = t1 - t0
    check1 = time == dist
    check2 = time > dist and (time - dist) % 2 == 0
    if not (check1 or check2):
        success = False
        break
    (t0, x0, y0) = (t1, x1, y1)
if success:
    print('Yes')
else:
    print('No')
