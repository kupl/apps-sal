H = int(input())


def attack(n):
    if 1 == n:
        return 1
    return 2 * attack(int(n / 2)) + 1


print((attack(H)))
