def main():
    n = int(input())
    t = input()
    v = 10 ** 10
    is_included = False
    first_threes = ['110', '101', '011']
    for first_three in first_threes:
        if t == first_three * (n // 3) + first_three[:n % 3]:
            is_included = True
            break
    if not is_included:
        print(0)
    elif t == '1':
        print(2 * v)
    elif t == '11':
        print(v)
    else:
        num_0 = t.count('0')
        if t[-1] == '0':
            print(v - num_0 + 1)
        else:
            print(v - num_0)


def __starting_point():
    main()


__starting_point()
