_ = input()
string = input()
lasts = {
    0: -1
}
curr_count = 0
best_best = 0
for idx, x in enumerate(string):
    if x == '1':
        curr_count += 1
    else:
        curr_count -= 1
    if curr_count in lasts:
        curr_best = idx - lasts[curr_count]
        if curr_best > best_best:
            best_best = curr_best
    else:
        lasts[curr_count] = idx
print(best_best)

"""
First try - Try to use something like binary search to find the length of the substring.
Sadly, this does not work,
    as knowing that the maximum possible substring length is 8 and having a valid substring of length 4 does not guarantee that we have a substring of length 6
    e.g 00111100
"""
"""
_ = input()
string = input()
str_len = len(string)
one_count, zero_count = 0, 0
counts_by_idx = {}
for idx, x in enumerate(string):
    if x == '1':
        one_count += 1
    else:
        zero_count += 1
    counts_by_idx[idx] = {'0': zero_count, '1': one_count}

maximum_substring_length = min(zero_count, one_count) * 2
print(maximum_substring_length)
curr_best = 0

lower_bound = 0
current_search = maximum_substring_length // 2
upper_bound = maximum_substring_length


def srch(lower_bound, current_search, upper_bound):
    nonlocal curr_best
    for start_idx in range(str_len-current_search):
        end_idx = start_idx + current_search
        zero_count = counts_by_idx[end_idx]['0'] - counts_by_idx[start_idx]['0']
        one_count = counts_by_idx[end_idx]['1'] - counts_by_idx[start_idx]['1']
        if one_count == zero_count:
            curr_best = zero_count * 2
            new_search = current_search + ((upper_bound - current_search) // 2)
            return current_search, new_search, upper_bound

    new_search = lower_bound + ((current_search - lower_bound) // 2)
    return lower_bound, new_search, current_search


while True:
    lower_bound, current_search, upper_bound = srch(lower_bound, current_search, upper_bound)
"""
