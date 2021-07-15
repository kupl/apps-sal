import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def is_prime(n):
        if n == 1:
            return False
        for k in range(2, int(pow(n, 0.5)) + 1):
            if n % k == 0:
                return False
        return True

    q = int(input())
    primes = set()
    nums = set()
    for i in range(2, 10 ** 5 + 1):
        if is_prime(i):
            primes.add(i)
            if (i + 1) // 2 in primes:
                nums.add(i)

    cnt = [0]
    for i in range(1, 10 ** 5 + 1):
        op = 1 if i in nums else 0
        cnt.append(cnt[-1] + op)

    for _ in range(q):
        l, r = list(map(int, input().split()))
        res = cnt[r] - cnt[l - 1]
        print(res)


def __starting_point():
    resolve()

__starting_point()
