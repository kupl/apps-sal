def bake(n, k, ai, bi):
    min_cookies = bi[0] // ai[0]
    for j in range(1, n):
        cookies = bi[j] // ai[j]
        if cookies < min_cookies:
            min_cookies = cookies
    possible = True
    while possible:
        cks = min_cookies + 1
        tenk = k
        for j in range(n):
            if bi[j] < (cks * ai[j]):
                tenk = tenk - ((cks * ai[j]) - bi[j])
                if tenk < 0:
                    possible = False
                    return min_cookies
        min_cookies = cks
    return min_cookies


def main():
    n, k = [int(i) for i in input().strip().split()]
    ai = [int(i) for i in input().strip().split()]
    bi = [int(i) for i in input().strip().split()]
    ans = bake(n, k, ai, bi)
    print(ans)


def __starting_point():
    main()


__starting_point()
