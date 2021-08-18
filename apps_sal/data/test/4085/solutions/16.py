q = int(input())


def eratosthene(n):
    if n < 2:
        return []
    n += 1
    tableau = [False, False] + [True] * (n - 2)
    tableau[2::2] = [False] * ((n - 2) // 2 + n % 2)
    premiers = [2]
    racine = int(n**0.5)
    racine = racine + [1, 0][racine % 2]
    for i in range(3, racine + 1, 2):
        if tableau[i]:
            premiers.append(i)
            tableau[i::i] = [False] * ((n - i) // i + int((n - i) % i > 0))
    for i in range(racine, n, 2):
        if tableau[i]:
            premiers.append(i)
    return premiers


primes = eratosthene(10**6 + 2)


def divisors(n):

    ans = 1
    for p in primes:
        tmp = 0
        if n % p == 0:
            while True:
                tmp += 1
                n //= p
                if n % p != 0:
                    break
        if tmp > 0:
            ans *= (tmp + 1)
            tmp = 0
        if p > n:
            break
    return ans - 2


for _ in range(q):

    n = int(input())
    l = sorted(list(map(int, input().split())))

    if n == 1:
        if l[0] in primes:
            print(l[0]**2)
        else:
            print(-1)

    elif n > 1:
        candidate = l[0] * l[-1]
        for i in range(1, n // 2):
            if l[i] * l[n - 1 - i] != candidate:
                print(-1)
                break
        else:
            if divisors(candidate) == n:
                if n % 2:
                    if l[n // 2]**2 == candidate:
                        print(candidate)
                    else:
                        print(-1)
                else:
                    print(candidate)
            else:
                print(-1)
