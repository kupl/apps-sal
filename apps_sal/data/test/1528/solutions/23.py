ip = input().split(" ")
n = int(ip[0])
x = int(ip[1])


def get_num_layers(level):
    if level == 1:
        return 5
    return 5 * (1 << (level - 1)) + 3 * ((1 << (level - 1)) - 1)


def func(level, index):
    if level == 1:
        return min(index - 1, 3)
    num_layers = get_num_layers(level)
    mid = num_layers // 2
    if index == mid + 1:
        return 1 + func(level - 1, mid - 1)
    if index == 1:
        return 0
    if index == num_layers:
        return 2 * func(level - 1, mid - 1) + 1
    if index <= mid:
        return func(level - 1, index - 1)
    if index > mid + 1:
        return 1 + func(level - 1, mid - 1) + func(level - 1, index - mid - 1)


print((func(n, x)))
