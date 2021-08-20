import math


def main():
    N = int(input())
    f = prime_factorize(N)
    cnt = 0
    if N == 1:
        print(cnt)
        return 0
    for p in f:
        prime = p[0]
        power = p[1]
        tmp = math.floor((math.sqrt(1 + 8 * power) - 1) / 2)
        cnt += tmp
    print(cnt)


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


main()
