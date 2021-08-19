T = int(input())
for i in range(T):
    t = input().split(' ')
    (n, x, y, d) = (int(t[0]), int(t[1]), int(t[2]), int(t[3]))
    if (y - x) % d == 0:
        print(abs(y - x) // d)
    else:
        (a, b) = (-1, -1)
        if (y - 1) % d == 0:
            a = (x - 1) // d + 1 + (y - 1) // d
        if (n - y) % d == 0:
            b = (n - x) // d + 1 + (n - y) // d
        if a == -1 and b == -1:
            print(-1)
        elif a == -1:
            print(b)
        elif b == -1:
            print(a)
        else:
            print(min(a, b))
