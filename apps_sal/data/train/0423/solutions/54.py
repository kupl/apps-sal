from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        prev_elem_dict = defaultdict(int)
        result = 0
        for num in arr:
            prev_elem_dict[num] = max(prev_elem_dict[num], prev_elem_dict[num - difference] + 1)
            result = max(result, prev_elem_dict[num])
        return result

