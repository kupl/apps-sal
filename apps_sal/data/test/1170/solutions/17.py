import math
import sys


def main():

    t = int(input())

    for i in range(t):
        ones = int(input())

        if ones == 0:
            print('1 1')
            continue

        gotem = False
        for j in range(1, ones):
            if j * j > ones:
                break
            if ones % j == 0:
                big = ones // j

                if (j + big) % 2 != 0:
                    continue
                else:
                    a = (j + big) // 2
                    b = big - a
                    if b <= 0:
                        continue
                    n = a
                    m = n // b

                    if n // m != b or n < 1 or m < 1:
                        continue

                    print('%d %d' % (n, m))
                    gotem = True
                    break

        if not gotem:
            print(-1)


def __starting_point():
    main()


__starting_point()
