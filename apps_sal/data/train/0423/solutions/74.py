from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        currentMax = 0
        dictionary = defaultdict(int)
        for i in range(len(arr)):
            dictionary[arr[i]] = dictionary[arr[i]-difference] + 1
        for e in dictionary:
            currentMax = max(dictionary[e], currentMax)
        return currentMax

