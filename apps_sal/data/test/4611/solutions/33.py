N = int(input())
(t, x, y) = (0, 0, 0)
ans = 'Yes'
for n in range(N):
    (ti, xi, yi) = map(int, input().split())
    dist = abs(xi - x) + abs(yi - y)
    dt = ti - t
    if dist > dt or (dist - dt) % 2 != 0:
        ans = 'No'
        break
    (t, x, y) = (ti, xi, yi)
print(ans)
