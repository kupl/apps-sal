for _ in range(int(input())):
    n = int(input())
    a, b, c = 0, 0, 0
    while n % 2 == 0:
        a += 1
        n //= 2
    while n % 3 == 0:
        a += 1
        b += 1
        n //= 3
    while n % 5 == 0:
        a += 2
        c += 1
        n //= 5
    if n > 1:
        print(-1)
    else:
        print(a + b + c)
