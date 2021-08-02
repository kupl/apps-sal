def main():
    n = int(input())
    c = str(input())

    w_count = 0
    for i in range(n):
        if c[i] == 'W':
            w_count += 1

    w_count_ano = 0
    for i in range(w_count):
        if c[- 1 - i] == 'W':
            w_count_ano += 1

    count = w_count - w_count_ano
    print(count)


def __starting_point():
    main()


__starting_point()
