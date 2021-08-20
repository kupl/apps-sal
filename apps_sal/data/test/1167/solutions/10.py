t = int(input())
for _ in range(t):
    (a, b, c, d, k) = map(int, input().split())
    x = (a - 1) // c + 1
    y = (b - 1) // d + 1
    if x + y <= k:
        print(x, y)
    else:
        print(-1)
