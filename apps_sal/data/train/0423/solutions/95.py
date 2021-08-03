class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        subseqs = dict()

        for num in arr:
            subseqs[num + difference] = subseqs.get(num, 0) + 1

        return max(subseqs.values())
