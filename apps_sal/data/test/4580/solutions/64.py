def index(rate):
    if rate <= 3199:
        idx = rate // 400
    else:
        idx = 'free'
    return idx


def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    color_lst = [0] * 8
    free = 0
    for i in range(n):
        rate = a_lst[i]
        idx = index(rate)
        if idx == 'free':
            free += 1
        else:
            color_lst[idx] = 1
    types = 0
    for i in range(8):
        if color_lst[i] == 1:
            types += 1
    if types > 0:
        minimum = types
    else:
        minimum = 1
    maximum = types
    max_add = free
    maximum += max_add
    print(minimum, maximum)


def __starting_point():
    main()


__starting_point()
