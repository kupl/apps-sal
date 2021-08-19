import sys
sys.setrecursionlimit(10001)


def main():
    m = int(input())
    temp = input().split()
    primes = [int(x) for x in temp]
    print(solver2(primes))


def solver2(primes):
    modulus = 10 ** 9 + 7
    primesDict = dict()
    for p in primes:
        if p not in primesDict:
            primesDict[p] = 1
        else:
            primesDict[p] += 1
    factors = 1
    for p in primesDict:
        factors *= primesDict[p] + 1
    if factors % 2 == 0:
        n = 1
        for p in primesDict:
            n = n * pow(p, primesDict[p], modulus) % modulus
        return pow(n, factors // 2, modulus)
    else:
        sqrtN = 1
        for p in primesDict:
            sqrtN = sqrtN * pow(p, primesDict[p] // 2, modulus) % modulus
        return pow(sqrtN, factors, modulus)


def expMod(n, e, modulus, recLimit=0):
    if e == 1:
        return n % modulus
    elif e % 2 == 0:
        return expMod(n, e // 2, modulus) ** 2 % modulus
    else:
        return n * expMod(n, e // 2, modulus) ** 2 % modulus


def digitCount(n):
    n = abs(n)
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


main()
