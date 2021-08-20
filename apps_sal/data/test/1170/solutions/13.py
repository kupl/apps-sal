from math import ceil
t = int(input())
for _ in range(t):
    x = int(input())
    if x == 1 or x % 4 == 2:
        print(-1)
    elif x == 0:
        print(1, 1)
    else:
        z = 0
        for i in range(ceil((x / 3) ** 0.5), ceil(x ** 0.5)):
            if x % i == 0 and (x // i - i) % 2 == 0:
                n = (i + x // i) // 2
                k = (x // i - i) // 2
                m = n // k
                if n // m == k:
                    print(n, m)
                    z = 1
                    break
        if z == 0:
            print(-1)
