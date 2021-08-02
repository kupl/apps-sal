import sys
lax = -10**9; lay = -10**9
for _ in range(int(input())):
    sign, x, y = list(map(str, sys.stdin.readline().split()))
    x = int(x)
    y = int(y)
    if sign == "+":
        if y > x:
            t = x
            x = y
            y = t
        lax = max(x, lax)
        lay = max(y, lay)
    else:
        if y > x:
            t = x
            x = y
            y = t
        # print(lax,lay)
        if lax <= x and lay <= y:
            print("YES")
        else:
            print("NO")
