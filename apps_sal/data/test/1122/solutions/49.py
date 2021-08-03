n, m = list(map(int, input().split()))

if n % 2 == 1:
    for i in range(m):
        print((n - i, i + 1))
else:
    used = [False] * (n + 1)
    offset = 0
    for i in range(m):
        a = n - (i + offset)
        b = i + offset + 1
        d = min(a - b, n - (a - b))
        if used[d] or a - b == n - (a - b):
            offset = 1
        used[d] = True
        print((n - i, i + offset + 1))
