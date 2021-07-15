t = int(input())
for i in range(t):
    n, x, y, d = list(map(int, input().split()))
    if abs(y - x) % d == 0 or y == 1 or y == n:
        print((abs(x - y) + d - 1) // d)
    else:
        if abs(y - 1) % d == 0 and abs(n - y) % d == 0:
            print(min((x - 1 + d - 1) // d + (y - 1) // d, (n - x + d - 1) // d + (n - y) // d))
        elif abs(y - 1) % d != 0 and abs(n - y) % d != 0:
            print(-1)
        elif abs(y - 1) % d == 0:
            print((x - 1 + d - 1) // d + (y - 1) // d)
        else:
            print((n - x + d - 1) // d + (n - y) // d)

