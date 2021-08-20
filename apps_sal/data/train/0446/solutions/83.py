from collections import Counter


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mapper = Counter(arr)
        count = 0
        size = len(mapper)
        values = sorted(mapper.values())
        for val in values:
            if val <= k:
                k -= val
                count += 1
            else:
                return size - count
        return size - count
