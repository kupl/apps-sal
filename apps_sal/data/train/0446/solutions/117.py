class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        from collections import Counter
        d = Counter(arr)
        q = sorted(arr, key=lambda x: (d[x], x))
        return len(set(q[k:]))
