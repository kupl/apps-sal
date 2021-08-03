N = int(input())


def calc(n):
    if n == 0:
        return 15
    if n == 1:
        return 14
    if n == 2:
        return 12
    if n == 3:
        return 13
    if n == 4:
        return 8
    if n == 5:
        return 9
    if n == 6:
        return 10
    if n == 7:
        return 11
    if n == 8:
        return 0
    if n == 9:
        return 1
    if n == 10:
        return 2
    if n == 11:
        return 3
    if n == 12:
        return 4
    if n == 13:
        return 5
    if n == 14:
        return 6
    if n == 15:
        return 7
    return 1 / 0


print(calc(N))
