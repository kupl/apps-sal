from collections import Counter


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        freq_sorted = sorted(arr, key=lambda x: (counter[x], x))
        return len(set(freq_sorted[k:]))
