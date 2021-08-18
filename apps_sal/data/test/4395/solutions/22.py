

def main():
    n = int(input())
    s = input()

    patterns = ['RGB', 'RBG', 'BGR', 'BRG', 'GRB', 'GBR']

    recolor_count = n + 1
    nice_pattern = None
    for p in patterns:
        curr_count = 0
        for i in range(n):
            if s[i] != p[i % 3]:
                curr_count += 1
        if curr_count < recolor_count:
            recolor_count = curr_count
            nice_pattern = p

    print(recolor_count)
    for i in range(n):
        print(nice_pattern[i % 3], end='')
    print()


def __starting_point():
    main()


__starting_point()
