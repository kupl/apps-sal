class Solution:
    def longestOnes(self, s: List[int], k: int) -> int:
        l = 0
        c_frequency = {0: 0, 1: 0}
        longest_str_len = 0
        for r in range(len(s)):

            if s[r] == 0:
                c_frequency[0] += 1
            else:
                c_frequency[1] += 1

            cells_count = r - l + 1
            if c_frequency[0] <= k or c_frequency[0] == 0:
                longest_str_len = max(longest_str_len, cells_count)

            else:
                if c_frequency[s[l]] != 0:
                    c_frequency[s[l]] -= 1
                l += 1

        return longest_str_len
