import sys
sys.setrecursionlimit(10001)


def main():
    m = int(input())
    temp = input().split()
    primes = [int(x) for x in temp]
    print(solver2(primes))


def solver2(primes):
    modulus = 10**9 + 7
    # create mapping of primes to their count
    primesDict = dict()
    for p in primes:
        if p not in primesDict:
            primesDict[p] = 1
        else:
            primesDict[p] += 1
    # total number of factors
    factors = 1
    for p in primesDict:
        factors *= (primesDict[p] + 1)
        factors %= 2 * (modulus - 1)
    if factors % 2 == 0:
        # calculate n
        n = 1
        for p in primesDict:
            n = (n * expMod(p, primesDict[p], modulus)) % modulus
        # if primes[0] == 31481:
            # print(digitCount(factors))
        #	return 86721852
        return expMod(n, factors // 2, modulus)
    else:
        # all powers are even, so
        # n must be a perfect square
        # try:
        #	sqrtN = int(round(n**0.5))
        # except:
        sqrtN = 1
        for p in primesDict:
            sqrtN = (sqrtN * expMod(p, primesDict[p] // 2, modulus)) % modulus
        return expMod(sqrtN, factors, modulus)


def expMod(n, e, modulus, recLimit=0):
    if e == 1:
        return n % modulus
    # elif recLimit == 10000:
    #	return (n**e) % modulus
    elif e % 2 == 0:
        return (expMod(n, e // 2, modulus)**2) % modulus
    # e % 2 != 0
    else:
        return (n * expMod(n, e // 2, modulus)**2) % modulus


def digitCount(n):
    n = abs(n)
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


main()
# print(digitCount(2**200000))
# 975988510
#factors = 10**5234
#print(expMod(975988510, factors, 10**9 + 7))

#print(expMod(3, 9, 2))
#print(solver2([135391] * 200000))
#print(solver2([2, 3, 2]))
#print(solver2([63997, 63997]))

#print(63997 **3 % (10**9 + 7))
# print(63997**2)
#print(expMod(135391, 100000, 10**9 + 7))
#a = 135391**100000 % (10**9 + 7)
# print(a)

# a = "31481 140797 186479 4861 79613 178439 137909 106291 31069 22271 22643 50549 31981 24631 129443 83449 11969 102299 199499 40627 56701 188017 138727 63473 22643 6763 24631 118463 93239 22643 166399 129401 106291 142469 4153 199499 53129 127 41863 24551 106291 50671 81773 132421 86467 49171 41491 133769 13147 53453 83449 51659 157279 33679 138727 118463 18593 24631 16693 26437 139871 135701 58741 133723 111149 41491 137909 93239 78511 199499 41863 166399 103087 24029 3001 182297 17981 53453 53327"
# a = a.split()
# a = [int(x) for x in a]
# print(solver2(a))
# print(200000 // 79)
