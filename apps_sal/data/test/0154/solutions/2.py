#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|
#  code

def main():
    k = int(input())
    s = [1, 2, 4, 5]
    i = 2
    while True:
        if s[-1] > int(1e6):
            break
        if s[i] % 2 == 0:
            s.append(2 * s[i] + 1)
            s.append(2 * s[i] + 2)
        else:
            s.append(2 * s[i] + 2)
            s.append(2 * s[i] + 3)
        i += 2
    if k in s:
        print(1)
    else:
        print(0)
    return


def __starting_point():
    main()


__starting_point()
