import math
import sys
input = sys.stdin.readline


def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def main():
    x = int(input())
    for i in range(x, 100004):
        if is_prime(i) == True:
            print(i)
            break


def __starting_point():
    main()


__starting_point()
