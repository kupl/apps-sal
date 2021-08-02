def main():
    n, k, *a = list(map(int, open(0).read().split()))

    cnt = [sum((x >> i) & 1 for x in a) for i in range(40)]
    bits = [0 if i > n - i else 1 for i in cnt]

    base = format(k, 'b')
    l = len(base)
    tmp = []

    if sum(2 ** i for i, b in enumerate(bits[:l]) if b == 1) > k:
        for i in range(l - 1, -1, -1):
            if int(base[-i - 1]) < bits[i]:
                bits[i] = 0
                tmp.append(sum(2 ** j for j, b in enumerate(bits[:l]) if b == 1))
    else:
        tmp.append(sum(2 ** j for j, b in enumerate(bits[:l]) if b == 1))

    ans = max(sum(i ^ x for x in a) for i in tmp if i <= k)
    print(ans)


def __starting_point():
    main()


__starting_point()
