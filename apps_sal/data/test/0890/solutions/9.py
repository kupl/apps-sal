def check_bits(x, n):
    total = 0
    for i in range(n):
        if x & 1 << i:
            total += 1
    return total >= 2


def check_compex(x, data, l, r, diff):
    total_c = 0
    min_c = None
    max_c = None
    for i in range(len(data)):
        if x & 1 << i:
            total_c += data[i]
            if min_c is None or min_c > data[i]:
                min_c = data[i]
            if max_c is None or max_c < data[i]:
                max_c = data[i]
    return l <= total_c <= r and max_c - min_c >= diff


def __starting_point():
    (n, l, r, diff) = list(map(int, input().split()))
    data = list(map(int, input().split()))
    total = 0
    for i in range(2 ** n):
        if check_bits(i, n) and check_compex(i, data, l, r, diff):
            total += 1
    print(total)


__starting_point()
