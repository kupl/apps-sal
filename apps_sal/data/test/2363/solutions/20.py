T = int(input())
for t in range(T):
    x, y = [int(n) for n in input().split()]
    ops = 0
    while x and y:
        if x < y:
            ops += int(y/x)
            y = y % x
        elif y < x:
            ops += int(x/y)
            x = x % y
        else:
            ops += 1
            break
    print(ops)
