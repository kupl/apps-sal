n = int(input())
b = list(map(int, input().split()))
lo = n + 1
if n <= 2:
    print(0)
    quit()
for i in range(-1, 2):
    for j in range(-1, 2):
        (bol, c) = (1, 0)
        if (b[0] + i - b[n - 1] - j) % (n - 1):
            continue
        d = -(b[0] + i - b[n - 1] - j) // (n - 1)
        for k in range(1, n - 1):
            d0 = b[k] - b[0] - i - d * k
            if abs(d0) > 1:
                bol = 0
                break
            elif d0:
                c += 1
        if bol:
            lo = min(c + abs(i) + abs(j), lo)
if lo > n:
    print(-1)
else:
    print(lo)
