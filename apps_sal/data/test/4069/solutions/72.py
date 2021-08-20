(x, k, d) = list(map(int, input().split()))
if x < 0:
    if x + k * d < 0:
        print(-x - k * d)
    else:
        a = -x // d
        x += a * d
        if (k - a) % 2 == 0:
            print(-x)
        else:
            print(x + d)
elif x - k * d > 0:
    print(x - k * d)
else:
    a = x // d
    x -= a * d
    if (k - a) % 2 == 0:
        print(x)
    else:
        print(d - x)
