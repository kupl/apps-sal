#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|
#  code

def main():
    from math import sqrt
    t = 1
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        if n % 2 == 0:
            print(n + k * 2)
        else:
            for i in range(3, n + 1):
                if n % i == 0:
                    print(n + i + (k - 1) * 2)
                    break
    return


def __starting_point():
    main()


__starting_point()
