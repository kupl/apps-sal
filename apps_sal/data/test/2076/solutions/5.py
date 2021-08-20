for _ in range(int(input())):
    (x, y, z) = list(map(int, input().split()))
    m = 0
    for a in range(x + 1):
        b = min(z // 2, y - 2 * a)
        m = max(m, 3 * (a + b))
    print(m)
