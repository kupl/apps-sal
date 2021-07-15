import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def make_divisors(n):
        divisors = []
        for i in range(1, int(pow(n, 0.5)) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        return divisors
    
    N = int(input())

    div_1 = make_divisors(N)
    res = 0
    for k in div_1:
        if k == 1:
            continue
        n = N
        while n > 1:
            if n % k == 0:
                n //= k
            else:
                if n >= k:
                    n %= k
                else:
                    n -= k
        if n == 1:
            res += 1

    div_2 = make_divisors(N - 1)
    res += len(div_2) - 1
    print(res)


def __starting_point():
    resolve()

__starting_point()
