n, m = map(int, input().split())

cakes = [[int(x) for x in input().split()] for _ in range(n)]

ans = 0
for i in range(8):
    cakes_sub = []
    key = [1, 1, 1]
    for j in range(3):
        if (i >> j) & 1:
            key[j] = -1.
    for j in range(n):
        k = [0] * 3
        for p in range(3):
            k[p] = key[p] * cakes[j][p]
        l = sum(k)
        cakes_sub.append([l] + k)
    cakes_sub.sort(reverse=True)
    a, b, c = 0, 0, 0
    for j in range(m):
        a += cakes_sub[j][1]
        b += cakes_sub[j][2]
        c += cakes_sub[j][3]
    sub = a + b + c
    if ans < sub:
        ans = sub

print(int(ans))
