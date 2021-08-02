n = int(input())
degs = [1]
cur = 1
while (cur < 1000000000):
    cur *= 2
    degs.append(cur)
for _ in range(n):
    k = int(input())
    ar = k * (k + 1) // 2
    # print(ar)
    pos = 0
    while degs[pos] <= k:
        pos += 1
    geom = 2 ** pos - 1
    # print(geom)
    print(ar - 2 * geom)
