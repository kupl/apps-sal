t = int(input())
for i in range(t):
    n, x, y, d = list(map(int, input().split()))
    if abs(x - y) % d == 0:
        print(abs(x - y) // d)
    else:
        res = 10000000000
        if (y - 1) % d == 0:
            res = min(res, -(-(x - 1) // d) + (y - 1) // d)
        if (n - y) % d == 0:
            res = min(res, -(-(n - x) // d) + (n - y) // d)
        if res == 10000000000:
            res = -1
        print(res)
