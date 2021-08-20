class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        sarr = sorted(arr, key=lambda x: (c[x], x))
        return len(set(sarr[k:]))
