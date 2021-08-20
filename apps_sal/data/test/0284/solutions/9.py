import sys


def __starting_point():
    n = int(input())
    for i in range(n // 1234567 + 1):
        cur = n - i * 1234567
        for j in range(cur // 123456 + 1):
            if (cur - j * 123456) % 1234 == 0:
                print('YES')
                return
    print('NO')


__starting_point()
