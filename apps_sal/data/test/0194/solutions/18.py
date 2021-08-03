def __starting_point():
    n, c1, c2 = list(map(int, input().split()))
    g = list(map(int, input().split()))
    count = 0
    deny = 0
    for i in range(n):
        if g[i] == 1:
            if c1 > 0:
                c1 -= 1
            elif c1 <= 0 and c2 > 0:
                c2 -= 1
                count += 1
            elif c2 <= 0 and count > 0:
                count -= 1
            else:
                deny += 1
        else:
            if c2 > 0:
                c2 -= 1
            else:
                deny += 2
    print(deny)


__starting_point()
