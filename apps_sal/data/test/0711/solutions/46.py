import sys

MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846


def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_ints2(x): return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a % b == 0 else GCD(b, a % b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)


def factorization(n):
    prime = []
    num = n
    p = 2
    while p * p <= n:
        cnt = 0
        while num % p == 0:
            cnt += 1
            num //= p
        prime.append((p, cnt))
        p += 1
    if num != 1:
        prime.append((num, 1))
    if not prime:
        prime.append((n, 1))

    return prime


def nCr(n, r, mod):
    a, b = 1, 1
    for i in range(r):
        a = a * (n - i) % mod
        b = b * (i + 1) % mod

    return a * pow(b, mod - 2, mod) % mod


def Main():
    n, m = read_ints()
    prime = factorization(m)
    ans = 1
    for p, num in prime:
        ans *= nCr(num + n - 1, num, MOD)
        ans %= MOD

    if m == 1:
        print(1)
    else:
        print(ans)


def __starting_point():
    Main()


__starting_point()
