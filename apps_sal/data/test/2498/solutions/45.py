from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_g(A):
    ret = 1
    for a in A:
        ret = lcm(ret, a)
    return ret


def is_hcm(x, A):
    for i in range(N):
        if x % A[i] != A[i] // 2:
            return False
    return True


N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

l = lcm_g(A)
if is_hcm(l // 2, A):
    ans = (2 * M + l) // (2 * l)
else:
    ans = 0

print(ans)
