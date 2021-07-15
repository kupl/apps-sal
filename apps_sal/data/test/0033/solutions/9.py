def extgcd(a, b):
    x, y = 0, 0
    d = a;
    if b != 0:
        d, y, x = extgcd(b, a%b)
        y -= (a//b) * x
    else:
        x, y = 1, 0
    return (d, x, y)

def main():
    a1, b1, a2, b2, L, R = map(int, input().split())
    g, k, l = extgcd(a1, a2);
    b = b2-b1;
    if (b%g != 0):
        print (0)
        return
    k *= b//g
    l *= -b//g
    low = -2**100
    high = 2**100
    while high-low > 1:
        med = (low+high)//2
        tk = k+med*a2//g
        tl = l+med*a1//g
        if (tk >= 0 and tl >= 0):
            high = med
        else:
            low = med
    k = k+high*a2//g
    x = a1*k+b1
    low = -1
    high = 2**100
    lcm = a1*a2//g
    while high - low > 1:
        med = (low+high)//2
        tx = x+med*lcm
        if tx >= L:
            high = med
        else:
            low = med
    x = x+high*lcm
    low = 0
    high = 2**100
    while high-low > 1:
        med = (low+high)//2
        tx = x+med*lcm
        if (tx <= R):
            low = med
        else:
            high = med
    if low == 0 and x > R:
        print (0)
        return
    print (low+1)
    return

def __starting_point():
    main()
__starting_point()
