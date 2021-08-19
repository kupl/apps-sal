(n, m) = list(map(int, input().split()))
max_height = 0
(prev_d, prev_h) = [0, 0]
for i in range(m):
    (d, h) = list(map(int, input().split()))
    if i == 0:
        max_height = d - 1 + h
        prev_d = d
        prev_h = h
        if i == m - 1:
            max_height = max(max_height, n - d + h)
        continue
    intersection = (-1 * (prev_d - prev_h) + (d + h)) / 2
    day = intersection - prev_h + prev_d
    if day > d or day < prev_d:
        max_height = -1
        break
    max_height = max(max_height, int(intersection))
    if i == m - 1:
        max_height = max(max_height, n - d + h)
    prev_d = d
    prev_h = h
if max_height >= 0:
    print(max_height)
else:
    print('IMPOSSIBLE')
