def main():
    l = input().split(' ')
    n, d = int(l[0]), int(l[1])
    k = input().split(' ')
    for x in range(0, n):
        k[x] = int(k[x])
    k.sort()
    m = int(input())
    sume = 0
    if n >= m:
        for x in range(0, m):
            sume = sume + k[x]
    else:
        for x in range(0, n):
            sume = sume + k[x]
        sume = sume - ((m - n) * d)
    print(sume)


def __starting_point():
    main()


__starting_point()
