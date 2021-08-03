from sys import stdin, stdout
m, n, k = [int(x) for x in stdin.readline().rstrip().split()]


large_prime = 10 ** 9 + 7


def fastPower(base, exp, mod):
    if exp == 0:
        x = 1
    else:
        half = fastPower(base, exp // 2, mod)
        x = half * half
        if exp % 2 == 1:
            x *= base
    return x % mod


def solve_two(n, m, k):
    if (m + n) % 2 == 1 and k == -1:
        print(0)
        return
    power1 = (m - 1) % (large_prime - 1)
    power2 = (n - 1) % (large_prime - 1)
    print(fastPower(2, power1 * power2, large_prime))
    return


solve_two(m, n, k)
