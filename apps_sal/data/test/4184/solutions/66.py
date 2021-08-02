def balance(weights: list, num: int) -> int:
    diff_list = []

    for i in range(0, num):
        group_l = weights[:i + 1]
        group_r = weights[i + 1:]
        diff_list.append(abs(sum(group_l) - sum(group_r)))
    diff_list.sort()
    return diff_list[0]


def __starting_point():
    n = int(input())
    weights = list(map(int, input().split()))
    print((balance(weights, n)))


__starting_point()
