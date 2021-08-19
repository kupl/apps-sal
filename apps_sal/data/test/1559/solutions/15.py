#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|
#  code

def main():
    l = int(input())
    s = input()
    n = len(s)

    if l > n or n % l != 0:
        k = '1' + '0' * (l - 1)
        c = (n + l - 1) // l
        print(k * c)
    else:
        k = s[:l]
        p = k * (n // l)
        if p > s:
            print(p)
        else:
            p = str(int(k) + 1)
            if len(p) == len(k):
                print(p * (n // l))
            else:
                n += 1
                k = '1' + '0' * (l - 1)
                c = (n + l - 1) // l
                print(k * c)
    return


def __starting_point():
    main()


__starting_point()
