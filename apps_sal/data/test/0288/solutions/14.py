from math import *


def main():
    n = int(input())
    (prev, fib) = (1, 2)
    count = 0
    while fib <= n:
        (prev, fib) = (fib, prev + fib)
        count += 1
    print(count)


main()
