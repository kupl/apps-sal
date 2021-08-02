n = int(input())
red = [tuple(map(int, input().split())) for _ in range(n)]
blue = [tuple(map(int, input().split())) for _ in range(n)]

red.sort(key=lambda x: x[1])
blue.sort()

count = 0
for xb, yb in blue:
    max_y = -1
    max_i = -1
    for i in range(n):
        xr, yr = red[i]
        if xb > xr and yb > yr and max_y < yr:
            max_y, max_i = yr, i
    if max_y >= 0:
        red[max_i] = (201, 201)
        count += 1
print(count)
