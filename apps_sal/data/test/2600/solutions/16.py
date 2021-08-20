tests = int(input())
for test in range(tests):
    (rows, cols) = list(map(int, input().split()))
    a = []
    for i in range(rows):
        b = list(map(int, input().split()))
        a.append(b)
    cnt = [[0 for j in range(2)] for i in range(rows + cols)]
    for r in range(rows):
        for c in range(cols):
            if r + c != rows + cols - r - c - 2:
                cnt[min(r + c, rows + cols - r - c - 2)][a[r][c]] += 1
    res = 0
    for i in cnt:
        res += min(i[0], i[1])
    print(res)
