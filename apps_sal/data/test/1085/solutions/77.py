def divisors(n):
    ret = set()
    for i in range(1, int(n ** 0.5) + 2):
        if n % i == 0:
            ret.add(i)
            ret.add(n // i)
    ret.remove(1)
    return ret


def main():
    N = int(input())
    s = divisors(N)
    ans = divisors(N - 1)
    for x in s:
        n = N
        if x == 1:
            continue
        while n % x == 0:
            n = n // x
        if n % x == 1:
            ans.add(x)
    print(len(ans))


main()
