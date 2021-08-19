def read_nums():
    return [int(x) for x in input().split()]


def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    vowels = 'aeiou'
    for (one, two) in zip(s, t):
        if (one in vowels) != (two in vowels):
            print('No')
            return
    print('Yes')


def __starting_point():
    main()


__starting_point()
