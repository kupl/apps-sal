def main():
    N = int(input())
    A = tuple(map(int, input().split()))

    MOD = 10 ** 9 + 7
    two_factor = 1
    ans = 0
    for i in range(60):
        bit_count = 0
        for a in A:
            if (a>>i) & 1:
                bit_count += 1
        ans += bit_count*(N-bit_count)*two_factor
        ans %= MOD
        two_factor *= 2
    print(ans)


def __starting_point():
    main()
__starting_point()
