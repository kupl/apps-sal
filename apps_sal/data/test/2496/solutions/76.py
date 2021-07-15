def main():
    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    N = int(input())
    A = [int(x) for x in input().strip().split()]
    maxA = max(A)
    if maxA == 1:
        print('pairwise coprime')
        return
    prime = [i if i % 2 != 0 else 2 for i in range(maxA+1)]
    f = [False] * (maxA+1)
    for i in range(3, int(maxA**.5)+1):
        if prime[i] != i:
            continue
        p = i * 2
        while p <= maxA:
            if prime[p] == p:
                prime[p] = i
            p += i

    def gcd(x, y):
        if y == 0:
            return x
        return gcd(y, x % y)

    setwise_coprime = A[0]
    for An in A[1:]:
        setwise_coprime = gcd(setwise_coprime, An)
        if setwise_coprime == 1:
            break
    # print(prime)
    for An in A:
        if An == 1:
            continue
        # print('An = {}'.format(An))
        not_pairwise_coprime = False
        while prime[An] != An:
            # print('prime[An]={}, f[prime[An]]={}'.format(prime[An], f[prime[An]]))
            if f[prime[An]]:
                not_pairwise_coprime = True
                break
            f[prime[An]] = True
            prime_An = prime[An]
            while An % prime_An == 0:
                An //= prime_An
        else:
            if An != 1:
                if f[An]:
                    not_pairwise_coprime = True
                else:
                    f[An] = True
        if not_pairwise_coprime:
            break
        # print(f)
    else:
        print('pairwise coprime')
        return
    if setwise_coprime == 1:
        print('setwise coprime')
    else:
        print('not coprime')

def __starting_point():
    main()
__starting_point()
