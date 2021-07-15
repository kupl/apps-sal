def main():
    N = int(input())
    all_non_zero, all_non_nine = 9 ** N, 9 ** N
    all_non_zeronine = 8 ** N
    any_zeronine = all_non_zero + all_non_nine - all_non_zeronine

    ans = 10 ** N - any_zeronine
    print((ans % (10 ** 9 + 7)))


def __starting_point():
    main()

__starting_point()
