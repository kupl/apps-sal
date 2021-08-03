def main():
    _ = int(input())
    a = [int(an) for an in input().split()]
    a.sort()
    half_val = -(-a[-1] // 2)
    dist_list = [abs(half_val - an) for an in a[:-1]]
    min_index = dist_list.index(min(dist_list))
    print(f'{a[-1]} {a[min_index]}')


def __starting_point():
    main()


__starting_point()
