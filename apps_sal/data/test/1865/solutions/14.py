def input_split(f):
    return list(map(f, input().split()))


def main():
    n = int(input())
    a = list(input_split(int))
    k = 0
    res = []
    for i in range(0, n - 1):
        m = a[i]
        index = 0
        for j in range(i + 1, n):
            if m > a[j]:
                m = a[j]
                index = j
        if m != a[i]:
            k += 1
            (a[i], a[index]) = (m, a[i])
            res.append((i, index))
    print(str(k))
    for v in res:
        print(' '.join(map(str, v)))


def __starting_point():
    main()


__starting_point()
