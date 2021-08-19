class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        truth_table = []
        for (idx, char) in enumerate(s):
            if char in ['a', 'e', 'i', 'o', 'u']:
                truth_table.append(idx)
        (pre_count, pre_idx, return_count) = (0, 0, 0)
        for (idx, vowel_idx) in enumerate(truth_table):
            if idx == 0:
                count = 1
                next_idx = idx + 1
            else:
                count = pre_count - 1
                next_idx = pre_idx + 1
            while next_idx < len(truth_table) and truth_table[next_idx] - vowel_idx + 1 <= k:
                count += 1
                pre_idx = next_idx
                next_idx += 1
            pre_count = count
            if count > return_count:
                return_count = count
        return return_count
