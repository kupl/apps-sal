from math import ceil
3.5
T = int(input())
for i in range(0, T):
    (n, x, y, d) = [*list(map(int, input().split()))]
    if y == 1 or y == n:
        print(int(ceil(abs(x - y) / d)))
    elif abs(x - y) % d == 0:
        print(abs(x - y) // d)
    elif (y - 1) % d == 0 and (n - y) % d == 0:
        ret1 = (y - 1) // d + int(ceil(abs(x - 1) / d))
        ret2 = (n - y) // d + int(ceil(abs(n - x) / d))
        print(min(ret1, ret2))
    elif (y - 1) % d == 0:
        print((y - 1) // d + int(ceil(abs(x - 1) / d)))
    elif (n - y) % d == 0:
        print((n - y) // d + int(ceil(abs(n - x) / d)))
    else:
        print(-1)
