#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|
#  code

def main():
    t = 1
    t = int(input())
    for _ in range(t):
        n, a, b, c, d = map(int, input().split())
        if n * (a + b) >= c - d and n * (a - b) <= c + d:
            print('Yes')
        else:
            print('No')
    return


def __starting_point():
    main()


__starting_point()
