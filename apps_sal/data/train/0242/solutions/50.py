from collections import defaultdict


class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        num_to_count = defaultdict(int)
        count_to_distinct_num = defaultdict(int)
        result = 0
        for (i, n) in enumerate(nums):
            prev_count = num_to_count[n]
            new_count = prev_count + 1
            num_to_count[n] = new_count
            if prev_count > 0:
                count_to_distinct_num[prev_count] -= 1
                if count_to_distinct_num[prev_count] == 0:
                    del count_to_distinct_num[prev_count]
            count_to_distinct_num[new_count] += 1
            if valid_prefix(count_to_distinct_num, new_count):
                result = i + 1
        return result


def valid_prefix(count_to_distinct_num, hint):
    assert len(count_to_distinct_num) > 0
    assert 0 not in count_to_distinct_num
    assert hint in count_to_distinct_num
    if 1 in count_to_distinct_num:
        if len(count_to_distinct_num) == 1:
            return True
        if len(count_to_distinct_num) == 2 and count_to_distinct_num[1] == 1:
            return True
    if len(count_to_distinct_num) == 1:
        if count_to_distinct_num[hint] == 1:
            return True
    if len(count_to_distinct_num) != 2:
        return False
    if hint - 1 in count_to_distinct_num:
        return count_to_distinct_num[hint] == 1
    if hint + 1 in count_to_distinct_num:
        return count_to_distinct_num[hint + 1] == 1
    return False
