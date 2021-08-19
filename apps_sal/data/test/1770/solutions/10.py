import math
for i in range(int(input())):
    (n, x, y, d) = list(map(int, input().split()))
    if y != n and y != 1:
        if abs(y - x) % d == 0:
            print(abs(y - x) // d)
        elif (y - 1) % d == 0:
            if (n - y) % d != 0:
                print(math.ceil((x - 1) / d) + (y - 1) // d)
            else:
                print(min(math.ceil((x - 1) / d) + (y - 1) // d, math.ceil((n - x) / d) + (n - y) // d))
        elif (n - y) % d != 0:
            print(-1)
        else:
            print(math.ceil((n - x) / d) + (n - y) // d)
    elif y == 1:
        print(math.ceil((x - 1) / d))
    else:
        print(math.ceil((n - x) / d))
