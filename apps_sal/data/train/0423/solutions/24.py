from collections import defaultdict


def lis(a, diff):
    lis = {}
    for i in range(len(a)):
        lis[a[i]] = lis.get(a[i] - diff, 0) + 1
    return max(lis.values())


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        return lis(arr, difference)
