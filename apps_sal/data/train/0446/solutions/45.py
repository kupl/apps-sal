from collections import Counter


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        arr = sorted(arr, key=lambda x: (count[x], x))
        return len(set(arr[k:]))
