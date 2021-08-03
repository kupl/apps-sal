import math


def prime_factorize(n):
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n = n // i
            ret.append([i, cnt])
    if n != 1:
        ret.append([n, 1])
    if len(ret) == 0:
        ret.append([n, 1])

    return ret


def main():
    A, B = [int(x) for x in input().split(" ")]
    g = math.gcd(A, B)
    pg = prime_factorize(g)
    if pg[0][0] == 1:
        print(1)
    else:
        print(len(pg) + 1)


main()
