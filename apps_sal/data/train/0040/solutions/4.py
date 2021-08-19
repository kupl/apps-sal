import sys as _sys


def main():
    q = int(input())
    for i_q in range(q):
        (n,) = _read_ints()
        a = tuple(_read_ints())
        result = find_min_sorting_cost(sequence=a)
        print(result)


def _read_line():
    result = _sys.stdin.readline()
    assert result[-1] == '\n'
    return result[:-1]


def _read_ints():
    return list(map(int, _read_line().split(' ')))


def find_min_sorting_cost(sequence):
    sequence = tuple(sequence)
    if not sequence:
        return 0
    indices_by_values = {x: [] for x in sequence}
    for (i, x) in enumerate(sequence):
        indices_by_values[x].append(i)
    borders_by_values = {x: (indices[0], indices[-1]) for (x, indices) in list(indices_by_values.items())}
    borders_sorted_by_values = [borders for (x, borders) in sorted(borders_by_values.items())]
    max_cost_can_keep_n = curr_can_keep_n = 1
    for (prev_border, curr_border) in zip(borders_sorted_by_values, borders_sorted_by_values[1:]):
        if curr_border[0] > prev_border[1]:
            curr_can_keep_n += 1
        else:
            if curr_can_keep_n > max_cost_can_keep_n:
                max_cost_can_keep_n = curr_can_keep_n
            curr_can_keep_n = 1
    if curr_can_keep_n > max_cost_can_keep_n:
        max_cost_can_keep_n = curr_can_keep_n
    return len(set(sequence)) - max_cost_can_keep_n


def __starting_point():
    main()


__starting_point()
