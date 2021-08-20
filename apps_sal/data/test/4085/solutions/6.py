def main():
    from sys import stdin, stdout

    def read():
        return stdin.readline().rstrip('\n')

    def read_array(sep=None, maxsplit=-1):
        return read().split(sep, maxsplit)

    def read_int():
        return int(read())

    def read_int_array(sep=None, maxsplit=-1):
        return [int(a) for a in read_array(sep, maxsplit)]

    def write(*args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join((str(a) for a in args)) + end)

    def write_array(array, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join((str(a) for a in array)) + end)

    def prime_sieve(n):
        """returns a sieve of primes >= 5 and < n"""
        flag = n % 6 == 2
        sieve = bytearray((n // 3 + flag >> 3) + 1)
        for i in range(1, int(n ** 0.5) // 3 + 1):
            if not sieve[i >> 3] >> (i & 7) & 1:
                k = 3 * i + 1 | 1
                for j in range(k * k // 3, n // 3 + flag, 2 * k):
                    sieve[j >> 3] |= 1 << (j & 7)
                for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                    sieve[j >> 3] |= 1 << (j & 7)
        return sieve

    def prime_list(n):
        """returns a list of primes <= n"""
        res = []
        if n > 1:
            res.append(2)
        if n > 2:
            res.append(3)
        if n > 4:
            sieve = prime_sieve(n + 1)
            res.extend((3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not sieve[i >> 3] >> (i & 7) & 1))
        return res
    primes = prime_list(10 ** 6)
    t = read_int()
    for _ in range(t):
        n = read_int()
        divisors = sorted(read_int_array())
        x = divisors[0] * divisors[-1]
        should_have = 1
        x2 = x
        for p in primes:
            if p > x2:
                break
            if x2 % p == 0:
                options = 1
                while x2 % p == 0:
                    options += 1
                    x2 //= p
                should_have *= options
        if should_have != n + 2:
            write(-1)
            continue
        (l, r) = (0, len(divisors) - 1)
        while l <= r:
            if divisors[l] * divisors[r] != x:
                write(-1)
                break
            l += 1
            r -= 1
        else:
            write(x)


main()
