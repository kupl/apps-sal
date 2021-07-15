def prime_factors(n):
    i = 2
    factors = []
    while i**2 <= n:
        if n % i != 0:
            i += 1
        else:
            factors.append(i)
            n = n // i
    if n > 1:
        factors.append(n)
    return factors

def resolve():
    N = int(input())
    import collections
    factors = collections.Counter(prime_factors(N))
    numbers = [0,1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9]
    cnt = 0
    for k, v in list(factors.items()):
        cnt += numbers[v]
    print(cnt)


if '__main__' == __name__:
    resolve()

