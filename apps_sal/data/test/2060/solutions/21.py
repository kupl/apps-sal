def main(x):
    b = x // 7
    a = 0
    while b * 7 + a * 3 != x:
        if b * 7 + a * 3 > x:
            b -= 1
        else:
            a += 1
        if b < 0:
            return "NO"
    return "YES"


def __starting_point():
    n = int(input())
    for i in range(n):
        print(main(int(input())))


__starting_point()
