def main():
    def calc_grundy(x, k):
        while True:
            if x < k:
                return 0
            rem, quot = x % k, x // k
            if rem == 0:
                return quot
            else:
                if rem <= quot + 1:
                    x -= quot + 1
                else:
                    x = quot * k + (rem % (quot + 1))

    n = int(input())
    ab = [list(map(int, input().split())) for _ in [0] * n]

    grundy = 0
    for a, b in ab:
        grundy = grundy ^ (calc_grundy(a, b))

    print((["Aoki", "Takahashi"][grundy > 0]))


main()
