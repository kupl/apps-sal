class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        sub_dict = {}
        n = len(arr)

        if n == 0:
            return 0
        if n == 1:
            return 1

        max_len = 1

        for i in range(n - 1, -1, -1):
            value = arr[i]
            new_k_v = []

            dd = value + difference
            if dd in sub_dict:
                sub_dict[value] = max(sub_dict.get(value, 0), sub_dict[dd] + 1)
                max_len = max(sub_dict[value], max_len)

            if value not in sub_dict:
                sub_dict[value] = 1

        return max_len
