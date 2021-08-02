def find_primes(n):
    ps = []
    t = [True] * n
    t[0] = t[1] = False
    for i in range(2, n):
        if not t[i]:
            continue
        ps.append(i)
        for j in range(i, n, i):
            t[j] = False
    return ps


def solve(string):
    n = int(string)
    if n == 1:
        return "0"
    rn = int(n**0.5 + 1)
    ps = find_primes(rn)
    ans = 0
    for i in ps:
        k = 1
        while n % (i**k) == 0:
            ans += 1
            n //= i**k
            k += 1
    return str(ans + (n >= rn))


def __starting_point():
    import sys
    print((solve(sys.stdin.read().strip())))


__starting_point()
