for _ in range(int(input())):
    n, x, y = list(map(int, input().split()))
    i = 1
    ad = []
    bd = []
    while i * i <= y - x:
        if (y - x) % i == 0:
            ad.append(i)
            if i * i != y - x:
                bd.append((y - x) // i)
        i += 1
    ds = ad + bd[::-1]
    best = (float("inf"), 0)
    for d in ds:
        l = (y - x) // d + 1
        if l > n:
            continue
        p = n - l
        while x - p * d <= 0:
            p -= 1
        best = min(best, (y + (n - l - p) * d, x - p * d))
    d = (best[0] - best[1]) // (n - 1)
    print(*list(range(best[1], best[0] + 1, d)))
