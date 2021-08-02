from fractions import gcd
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))


def two(n):
    ans = 0
    while n % 2 == 0:
        n //= 2
        ans += 1
    return ans


def multi_lcm(A):
    ans = A[0]
    for a in A:
        ans *= a // gcd(ans, a)
    return ans


def solve(N, M, A):
    ans = 0
    num_two = len(set(map(two, A)))
    if num_two != 1:
        return 0
    l = multi_lcm(A)
    ans = (M + l // 2) // l
    return ans


print((solve(N, M, A)))
