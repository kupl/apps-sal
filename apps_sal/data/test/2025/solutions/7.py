

def m(n):
    if n == 9:
        return 1
    elif n < 4:
        return -1
    c = 0
    if n % 2:
        if n >= 13:
            c += 1
            n -= 9
        else:
            return -1
    if not ((n - 2) % 4):
        n -= 2
    if not n % 4:
        return c + n // 4


def __starting_point():
    for i in range(int(input())):
        print(m(int(input())))


__starting_point()
