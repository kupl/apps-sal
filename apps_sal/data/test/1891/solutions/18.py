from collections import Counter
from functools import reduce

n, k, A, B = list(map(int, input().split()))

positions = sorted(list([int(s) - 1 for s in input().split()]))

d_h_counts = Counter(positions)
h_indices = d_h_counts

for ind in h_indices:
    h_indices[ind] = (B * h_indices[ind], h_indices[ind])


ind_filled = sorted(h_indices)


def reduce(ind_filled, d_values, ll):
    """
    Merge adjacent non-empty blocks and compute the indices of the new non-empty blocks
    :param d_values:
    :return:
    """

    index = 0
    d_res = {}
    out_ind = []
    while index < len(ind_filled):

        ai = ind_filled[index]

        if index == len(ind_filled) - 1 or ind_filled[index] // 2 != ind_filled[index + 1] // 2:
            d_res[ai // 2] = (min(A + d_values[ai][0], d_values[ai][1] * B * 2 * ll), d_values[ai][1])
            out_ind.append(ai // 2)
            index += 1

        elif ind_filled[index] // 2 == ind_filled[index + 1] // 2:
            anext = ind_filled[index + 1]
            d_res[ai // 2] = (min(d_values[ai][0] + d_values[anext][0],
                                  (d_values[ai][1] + d_values[anext][1]) * B * 2 * ll),
                              d_values[ai][1] + d_values[anext][1])
            out_ind.append(ai // 2)

            index += 2

    return out_ind, d_res


ll = 1

arr_ind = ind_filled

npow = 0

while npow < n:

    arr_ind, d_h_counts = reduce(arr_ind, d_h_counts, ll)

    ll *= 2
    npow += 1


k = list(d_h_counts.keys())[0]
print(d_h_counts[k][0])
