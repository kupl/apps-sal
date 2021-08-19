modulus = 10 ** 9 + 7


def main():
    (n, x) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    total = sum(arr)
    powers = [total - x for x in arr]
    powers.sort(reverse=True)
    while True:
        low = powers[len(powers) - 1]
        cnt = 0
        while len(powers) > 0 and powers[len(powers) - 1] == low:
            cnt += 1
            powers.pop()
        if cnt % x == 0:
            cnt = cnt // x
            for i in range(cnt):
                powers.append(low + 1)
        else:
            low = min(low, total)
            print(pow(x, low, modulus))
            return


def __starting_point():
    main()


__starting_point()
