t = int(input())
for _ in range(t):
    (n, x) = list(map(int, input().split()))
    a = b = -1100100100100
    for i in range(n):
        (d, h) = list(map(int, input().split()))
        a = max(a, d - h)
        b = max(b, d)
    if x <= b:
        print(1)
    elif a <= 0:
        print(-1)
    else:
        x -= b
        print((x + a - 1) // a + 1)
