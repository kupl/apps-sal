for _ in range(int(input())):
    (n, x, a, b) = [int(i) for i in input().split(' ')]
    (a, b) = (min(a, b), max(a, b))
    while x:
        if a > 1:
            a -= 1
        elif b < n:
            b += 1
        x -= 1
    print(b - a)
