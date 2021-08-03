from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        count_dict = defaultdict(int)
        for num in arr:
            count_dict[num] = count_dict[num - difference] + 1
        return max(count_dict.values())
