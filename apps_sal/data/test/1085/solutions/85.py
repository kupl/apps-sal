import math


def calc_yakusu_num(n):
    num = 0

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n // i:
                num += 1
            else:
                num += 2
    return num - 1


def calc_yakusu(n):
    yakusu = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n // i:
                yakusu.append(i)
            else:
                if i != 1:
                    yakusu.append(i)
                yakusu.append(n // i)
    return yakusu


def __starting_point():
    ans = 0
    n = int(input())

    ans += calc_yakusu_num(n - 1)

    y = calc_yakusu(n)

    for i in y:
        tmp = n
        while tmp % i == 0:
            tmp //= i
        if tmp % i == 1:
            ans += 1
    print(ans)


__starting_point()
