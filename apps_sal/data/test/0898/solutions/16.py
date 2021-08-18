import sys


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


input = sys.stdin.readline
N, M = (int(i) for i in input().split())
M_div = make_divisors(M)
div_rev = M_div[::-1]

for i in range(len(M_div)):
    if N <= M_div[i]:
        print(div_rev[i])

        break
