
n, a, b = list(map(int, input().strip().split()))


if a + b < n:
    print(0)
else:
    x = 2
    while True:
        if a // x + b // x >= n and a // x >= 1 and b // x >= 1:
            x += 1
        else:
            print(x - 1)
            break

