def prime_factorization(x):
    """素因数分解"""
    import math
    re = []
    i = 2
    while x != 1:
        if x % i == 0:
            re.append(i)
            x //= i
        else:
            i += 1
            if i > math.sqrt(x):
                re.append(x)
                break
    return re


def solve(N):
    pf = []
    for i in range(1, N + 1):
        pf += prime_factorization(i)
    pf_nums = [0] * (N + 1)
    for p in pf:
        pf_nums[p] += 1

    def num(m):
        return len([i for i in pf_nums if i >= m - 1])
    ans = num(75) + num(25) * (num(3) - 1) + num(15) * (num(5) - 1) + num(5) * (num(5) - 1) * (num(3) - 2) // 2
    print(ans)


def __starting_point():
    N = int(input())
    solve(N)


__starting_point()
