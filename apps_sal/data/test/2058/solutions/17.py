def main():
    a = input()
    b = input()
    total_comparable = len(b) - len(a) + 1
    if total_comparable < 1:
        print(0)
        return
    cumulitive_one_b = [0] * len(b)
    for i in range(len(b)):
        if i != 0:
            cumulitive_one_b[i] += cumulitive_one_b[i - 1]
        if b[i] == '1':
            cumulitive_one_b[i] += 1
    hamming_distance = 0
    for i in range(len(a)):
        start = i
        end = i + total_comparable - 1
        if start == 0:
            total_comparable_one = cumulitive_one_b[end]
        else:
            total_comparable_one = cumulitive_one_b[end] - cumulitive_one_b[start - 1]
        if a[i] == '0':
            hamming_distance += total_comparable_one
        else:
            hamming_distance += total_comparable - total_comparable_one
    print(hamming_distance)


def __starting_point():
    main()


__starting_point()
