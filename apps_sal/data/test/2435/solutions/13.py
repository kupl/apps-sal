t = int(input())
for _ in range(t):
    n, x, m = list(map(int, input().split()))
    mi, ma = x, x + 1
    for i in range(m):
        l, r = list(map(int, input().split()))
        r += 1
        if l <= mi < r or l < ma <= r:
            mi = min(mi, l)
            ma = max(ma, r)
    print(ma - mi)
