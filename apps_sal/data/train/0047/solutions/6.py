INF = 10 ** 15
for _ in range(int(input())):
    (n, q) = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    a = -INF
    b = 0
    for i in arr:
        if a == -INF:
            c = 0
            d = i
        else:
            c = b - i
            d = a + i
        (a, b) = (max(a, c), max(b, d))
    print(max(a, b))
