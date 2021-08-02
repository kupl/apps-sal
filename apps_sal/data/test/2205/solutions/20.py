
def main():
    n = int(input())
    p = list(map(int, input().split()))

    xor = [0 for i in range(n + 1)]
    for i in range(n):
        xor[i + 1] = xor[i] ^ (i + 1)

    ans = 0
    for i in range(n):
        ans ^= p[i]

    for i in range(n):
        a = n % (2 * (i + 1))
        if a >= i + 1:
            ans ^= xor[i] ^ xor[a - (i + 1)]
        else:
            ans ^= xor[a]
    print(ans)


def __starting_point():
    main()


__starting_point()
