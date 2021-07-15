def main():
    p, q = list(map(int, input().split()))
    lim = 1179860
    sieve = [0, q] * (lim // 2)
    for i in range(3, int(lim ** .5) + 1, 2):
        if sieve[i]:
            for j in range(i * i, lim, i):
                sieve[j] = 0
    sieve[1], sieve[2] = -p, q - p
    for i in range(3, 10):
        sieve[i] -= p
    for s in map(str, (list(range(1, 1000)))):
        ss = (s, s[::-1])
        for m in '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
            i = int(m.join(ss))
            if i < lim:
                sieve[i] -= p
    res = b = 0
    for i, a in enumerate(sieve):
        b += a
        if b <= 0:
            res = i
    print(res)


def __starting_point():
    main()

__starting_point()
