for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    x = min(a, b)
    y = max(a, b)
    c = 0
    if x == y:
        print(0)
    else:
        c += (y - x) // 5
        rem = (y - x) % 5
        c += rem // 2
        rem = rem % 2
        c += rem
        print(c)
