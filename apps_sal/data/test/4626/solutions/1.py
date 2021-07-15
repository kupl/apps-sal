for _ in range(int(input())):
    a,b,c = map(int, input().split())
    pd = abs(a-b) + abs(b-c) + abs(a-c)
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                a1, b1, c1 = a+x, b+y, c+z
                pd = min(pd, abs(a1-b1) + abs(b1-c1) + abs(a1-c1))
    print(pd)
