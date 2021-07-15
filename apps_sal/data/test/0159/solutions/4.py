from fractions import gcd


def is_co_prime(x, y):
    return gcd(x, y) != 1


def solve():
    N = int(input())
    L = list(map(int, input().split()))

    ans = [str(L[0])]

    x = 0
    for i in range(1, N):
        if is_co_prime(L[i], L[i - 1]):
            x += 1
            ans.append('1')
        ans.append(str(L[i]))

    print(x)
    print(' '.join(ans))


def __starting_point():
    solve()

__starting_point()
