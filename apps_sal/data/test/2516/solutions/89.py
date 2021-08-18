def main():
    N, p = list(map(int, input().split()))
    S = input()
    S = S[::-1]

    if p == 2 or p == 5:
        ans = 0
        for i, s in enumerate(S):
            if int(s) % p == 0:
                ans += N - i
        print(ans)
    else:
        modp_counter = [0] * p
        modp = 0
        modp_counter[0] = 1
        pair_count = 0
        d = 1
        for s in S:
            modp = (int(s) * d % p + modp) % p
            pair_count += modp_counter[modp]
            modp_counter[modp] += 1
            d *= 10
            d %= p
        print(pair_count)


main()
