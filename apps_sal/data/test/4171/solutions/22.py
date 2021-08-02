MAX = 2 * 10 ** 5


def main():
    n, k = list(map(int, input().split()))
    a = sorted(map(int, input().split()))

    ops = [0] * (MAX + 1)
    ks = [0] * (MAX + 1)

    for x in a:
        c = x
        j = 0

        while True:
            if ks[c] < k:
                ops[c] += j
                ks[c] += 1

            if c == 0:
                break

            c //= 2
            j += 1

    min_ops = float('inf')
    for i in range(MAX + 1):
        if ks[i] == k:
            min_ops = min(ops[i], min_ops)

    print(min_ops)


main()
