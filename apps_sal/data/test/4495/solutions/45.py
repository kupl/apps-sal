a, b, x = tuple([int(x) for x in input().split(" ")])
if a % x == 0:
    print((b // x - a // x + 1))
else:
    print((b // x - a // x))

