def main():
    n, m = input().split(' ')
    n = int(n)
    m = int(m)
    res = 0
    if n < m:
        print("-1")
    else:
        if n % 2 != 0:
            n -=1
            res += 1
        shag_count2 = n / 2
        if (shag_count2 + res) % m == 0:
            print(int(shag_count2 + res))
        else:
            while (shag_count2 + res) % m != 0:
                res += 1
            print(int(shag_count2 + res))


def __starting_point():
    main()

__starting_point()
