t = int(input())
for _ in range(t):
    (x, y) = list(map(int, input().split()))
    (a, b) = list(map(int, input().split()))
    cst = 0
    if 2 * a > b:
        cst += b * min(x, y)
        e = min(x, y)
        x -= e
        y -= e
    cst += a * x + a * y
    print(cst)
