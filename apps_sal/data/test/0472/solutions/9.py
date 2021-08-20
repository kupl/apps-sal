import math


def digit_sum(n):
    su = 0
    while n:
        su += n % 10
        n = math.floor(n / 10)
    return su


def main():
    n = int(input())
    mini = -1
    for s in range(1, 9 * 10 + 1):
        a = (-s + math.sqrt(s * s + 4 * n)) / 2
        b = (-s - math.sqrt(s * s + 4 * n)) / 2
        x = math.floor(a)
        y = math.floor(b)
        if a.is_integer() and x != 999959999 and (x > 0) and (digit_sum(x) == s) and (mini == -1 or x < mini):
            mini = x
        if b.is_integer() and x != 999959999 and (y > 0) and (digit_sum(y) == s) and (mini == -1 or y < mini):
            mini = y
    print(mini)


def __starting_point():
    main()


__starting_point()
