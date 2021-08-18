import math


def getLnInput():
    return input().split()


def ceilDivision(a, b):
    return (a - 1) // b + 1


def isPrime(n):
    if n < 1:
        return False
    if n == 2:
        return True
    flg = True
    for i in range(2, math.ceil(math.sqrt(n + 1))):
        if n % i == 0:
            flg = False
            break
    return flg


def main():
    n = int(getLnInput()[0])
    if n < 4:
        print(1)
    elif isPrime(n):
        print(1)
    elif n % 2 == 0:
        print(2)
    else:
        if isPrime(n - 2):
            print(2)
        else:
            print(3)
    return


main()
