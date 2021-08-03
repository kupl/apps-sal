n = int(input())


def solve(n):
    mod = 10 ** 9 + 7
    As = [1, 2, 3]
    ABCs = [a + b + c for a in As for b in As for c in As]
    k = len(ABCs)
    m = 20

    return (pow(k, n, mod) - pow(7, n, mod)) % mod


print(solve(n))
