def check(num_str: str) -> int:
    n = len(num_str)
    diff_lists = []
    for i in range(0, n - 2):
        diff_lists.append(abs(int(num_str[i] + num_str[i + 1] + num_str[i + 2]) - 753))
    diff_lists.sort()

    return (diff_lists[0])


def __starting_point():
    s = input()
    print((check(s)))


__starting_point()
