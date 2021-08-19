_ = input()
string = input()
lasts = {0: -1}
curr_count = 0
best_best = 0
for (idx, x) in enumerate(string):
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
'\nFirst try - Try to use something like binary search to find the length of the substring.\nSadly, this does not work,\n    as knowing that the maximum possible substring length is 8 and having a valid substring of length 4 does not guarantee that we have a substring of length 6\n    e.g 00111100\n'
"\n_ = input()\nstring = input()\nstr_len = len(string)\none_count, zero_count = 0, 0\ncounts_by_idx = {}\nfor idx, x in enumerate(string):\n    if x == '1':\n        one_count += 1\n    else:\n        zero_count += 1\n    counts_by_idx[idx] = {'0': zero_count, '1': one_count}\n\nmaximum_substring_length = min(zero_count, one_count) * 2\nprint(maximum_substring_length)\ncurr_best = 0\n\nlower_bound = 0\ncurrent_search = maximum_substring_length // 2\nupper_bound = maximum_substring_length\n\n\ndef srch(lower_bound, current_search, upper_bound):\n    nonlocal curr_best\n    for start_idx in range(str_len-current_search):\n        end_idx = start_idx + current_search\n        zero_count = counts_by_idx[end_idx]['0'] - counts_by_idx[start_idx]['0']\n        one_count = counts_by_idx[end_idx]['1'] - counts_by_idx[start_idx]['1']\n        if one_count == zero_count:\n            # Try to go up\n            curr_best = zero_count * 2\n            new_search = current_search + ((upper_bound - current_search) // 2)\n            return current_search, new_search, upper_bound\n\n    new_search = lower_bound + ((current_search - lower_bound) // 2)\n    return lower_bound, new_search, current_search\n\n\nwhile True:\n    lower_bound, current_search, upper_bound = srch(lower_bound, current_search, upper_bound)\n"
