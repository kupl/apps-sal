a = list(map(int, input().split()))

ans = 'NO'
pairs = [[1, 9], [5, 21], [13, 17]]
cells = {
    1: [5, 6, 17, 18, 21, 22, 13, 14],
    9: [7, 8, 19, 20, 23, 24, 15, 16],
    5: [9, 10, 19, 17, 4, 3, 14, 16],
    21: [11, 12, 20, 18, 2, 1, 13, 15],
    13: [7, 5, 3, 1, 22, 24, 11, 9],
    17: [8, 6, 4, 2, 21, 23, 12, 10],
}

for i, j in pairs:
    if 1 < len(set(a[i - 1: i + 3])) or 1 < len(set(a[j - 1: j + 3])):
        continue
    ci = cells[i]
    cj = cells[j]
    for d in [2, 6]:
        f = True
        for k in range(0, 8, 2):
            if a[ci[k] - 1] != a[ci[(k + 1) % 8] - 1]:
                f = False
            if a[cj[k] - 1] != a[cj[(k + 1) % 8] - 1]:
                f = False
            if a[ci[k] - 1] != a[cj[(k + d) % 8] - 1]:
                f = False
        if f:
            ans = 'YES'

print(ans)

