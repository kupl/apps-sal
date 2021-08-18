def do():
    n = int(input())
    s = input()
    if s == "1":
        print((2 * 10**10))
        return
    if s == "0":
        print((1 * 10 ** 10))
        return
    if s == "10":
        print((1 * 10 ** 10))
        return

    def do(offset):
        can = True
        x = 0
        if offset == 1 or offset == 2:
            x += 1
        for i in range(n):
            offset %= 3
            if offset == 0 or offset == 1:
                if s[i] == "1":
                    offset += 1
                    continue
                else:
                    can = False
            if offset == 2:
                if s[i] == "0":
                    offset += 1
                    if i > 1 and s[i - 2] == s[i - 1] == "1":
                        x += 1
                    continue
                else:
                    can = False
        if offset == 1 or offset == 2:
            x += 1
        return can, x

    for i in range(3):
        can, x = do(i)
        if can:
            print((10**10 - x + 1))
            return
    print((0))


do()
