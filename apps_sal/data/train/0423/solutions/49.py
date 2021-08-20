import collections


class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        prev_seq = collections.defaultdict(int)
        max_seq = 1
        for x in reversed(arr):
            target = x + difference
            x_seq = prev_seq[target] + 1
            max_seq = max(max_seq, x_seq)
            prev_seq[x] = max(prev_seq[x], x_seq)
        return max_seq
