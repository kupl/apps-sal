

import sys

cache = {}

def max_possible(pie_slices, current_slice, pre_sums):

    if current_slice in cache:
        return cache[current_slice]

    if len(pie_slices) - 1 == current_slice:
        return pie_slices[current_slice]


    max_score = -1
    for cs in range(current_slice, len(pie_slices) - 1):
        score = pie_slices[cs] + pre_sums[cs + 1] - max_possible(pie_slices, cs + 1, pre_sums)

        if score > max_score:
            max_score = score

    # if the last element gives the highest score
    if max_score < pie_slices[-1]:
        max_score = pie_slices[-1]

    cache[current_slice] = max_score

    return max_score

def main():
    n = int(sys.stdin.readline().strip())

    pie_slices = [int(tok) for tok in sys.stdin.readline().strip().split()]

    pre_sums = [sum(pie_slices[i:]) for i in range(len(pie_slices))]

    b = max_possible(pie_slices, 0, pre_sums)
    print(sum(pie_slices) - b, b)








def __starting_point():
    main()

__starting_point()
