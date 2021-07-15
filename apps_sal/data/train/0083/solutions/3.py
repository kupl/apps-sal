for __ in range(int(input())):
    x, y, a, b = map(int, input().split())
    z = y - x
    c = a + b
    print(-1 if z % c else z // c)
