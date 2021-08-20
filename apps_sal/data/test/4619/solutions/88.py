(W, H, N) = list(map(int, input().split()))
max_x = 0
max_y = 0
min_x = W
min_y = H
for i in range(N):
    (x, y, a) = list(map(int, input().split()))
    if a == 1:
        max_x = max(max_x, x)
    elif a == 2:
        min_x = min(min_x, x)
    elif a == 3:
        max_y = max(max_y, y)
    else:
        min_y = min(min_y, y)
if min_x > max_x and min_y > max_y:
    print((min_x - max_x) * (min_y - max_y))
else:
    print(0)
