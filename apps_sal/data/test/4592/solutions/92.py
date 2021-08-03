import collections


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def main():
    dd = collections.defaultdict(int)
    n = int(input())
    MOD = 10**9 + 7

    for i in range(1, n + 1):
        k = factorization(i)
        for j in k:
            dd[j[0]] += j[1]
    res = 1
    for j in list(dd.keys()):
        if(j != 1):
            res *= (dd[j] + 1) % MOD
            res %= MOD
    print(res)


def __starting_point():
    main()


__starting_point()
