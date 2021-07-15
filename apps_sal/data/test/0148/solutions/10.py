def main():
    n, a,x,b,y = map(int, input().strip().split())
    a -= 1
    x -= 1
    b -= 1
    y -= 1
    cf = a
    cs = b

    if a == b:
        print('YES')
        return
    while cf != x and cs != y:
        cf += 1
        cf %= n
        cs += (n - 1)
        cs %= n
        if cf == cs:
            print('YES')
            return
    print('NO')
    return

def __starting_point():
    main()
__starting_point()
