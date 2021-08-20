from collections import defaultdict
(h, w, n) = list(map(int, input().split()))
d = defaultdict(int)
surround = [(0, 0), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
for _ in range(n):
    (x, y) = list(map(int, input().split()))
    x -= 1
    y -= 1
    for i in surround:
        if x + i[0] >= h or x + i[0] < 0 or y + i[1] < 0 or (y + i[1] >= w):
            continue
        else:
            d[x + i[0], y + i[1]] += 1
num = [0] * 10
for key in d:
    if key[0] >= 1 and key[0] < h - 1 and (key[1] >= 1) and (key[1] < w - 1):
        num[d[key]] += 1
num[0] = (h - 2) * (w - 2) - sum(num)
for ans in num:
    print(ans)
