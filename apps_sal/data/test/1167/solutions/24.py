t = int(input())
for _ in range(t):
    a, b, c, d, k = list(map(int, input().split()))
    x = (a + c - 1) // c
    y = (b + d - 1) // d

    if x + y <= k:
        print(x, y)
    else:
        print(-1)
