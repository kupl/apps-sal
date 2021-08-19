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


def solve(N, A):
    ans = 0
    for a in A:
        while a % 2 == 0:
            ans += 1
            a //= 2
    print(ans)


def __starting_point():
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)


__starting_point()
