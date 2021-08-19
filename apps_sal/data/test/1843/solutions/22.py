T = int(input())
for _ in range(T):
    N = int(input())
    tmpN = N
    p = 0
    while tmpN > 0:
        tmpN = tmpN >> 1
        p += 1
    x = N * (N + 1) // 2
    y = (1 << p + 1) - 2
    print(x - y)
