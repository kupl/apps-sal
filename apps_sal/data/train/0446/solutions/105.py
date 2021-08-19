from collections import Counter


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqDict = Counter(arr)
        values = sorted(list(freqDict.values()))
        sumForK = 0
        for (idx, value) in enumerate(values):
            if sumForK + value == k:
                return len(values) - idx - 1
            elif sumForK + value > k:
                return len(values) - idx
            sumForK += value
        return 0
