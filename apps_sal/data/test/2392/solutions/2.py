MODULO = 1000000007


def main():
    n = int(input())
    tot_ans = 0
    for a7 in range(1, n - 11):
        k = n - a7
        if not k % 2 == 0:
            continue
        k = k / 2
        ans = (k - 1) * (k - 2) * (k - 3) * (k - 4) * (k - 5)
        ans = ans / 120
        ans = ans % MODULO
        tot_ans = (tot_ans + ans) % MODULO
    print(str(tot_ans))


def __starting_point():
    main()


__starting_point()
