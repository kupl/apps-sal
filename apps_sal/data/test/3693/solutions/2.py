n = 4
a = list(map(int, input().split()))

am0 = min(a[0], a[2], a[4], a[6])
am1 = max(a[0], a[2], a[4], a[6])
aM0 = min(a[1], a[3], a[5], a[7])
aM1 = max(a[1], a[3], a[5], a[7])

b = list(map(int, input().split()))

bm0 = min(b[0], b[2], b[4], b[6])
bm1 = max(b[0], b[2], b[4], b[6])
bM0 = min(b[1], b[3], b[5], b[7])
bM1 = max(b[1], b[3], b[5], b[7])

for i in range(5):
    if i < 4:
        x, y = b[2 * i], b[2 * i + 1]
    else:
        x, y = (bm0 + bm1) / 2, (bM0 + bM1) / 2
    if am0 <= x <= am1 and aM0 <= y <= aM1:
        print('YES')
        return

b = [
        (b[0] - b[1], b[0] + b[1]),
        (b[2] - b[3], b[2] + b[3]),
        (b[4] - b[5], b[4] + b[5]),
        (b[6] - b[7], b[6] + b[7]),
        ]
bm0 = min(b[0][0], b[1][0], b[2][0], b[3][0])
bm1 = max(b[0][0], b[1][0], b[2][0], b[3][0])
bM0 = min(b[0][1], b[1][1], b[2][1], b[3][1])
bM1 = max(b[0][1], b[1][1], b[2][1], b[3][1])

for i in range(5):
    if i < 4:
        x, y = a[2 * i], a[2 * i + 1]
    else:
        x, y = (am0 + am1) / 2, (aM0 + aM1) / 2
    x, y = x - y, x + y
    if bm0 <= x <= bm1 and bM0 <= y <= bM1:
        print('YES')
        return

print('NO')

