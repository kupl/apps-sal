class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        arr = list(reversed([item for (items, c) in count.most_common() for item in [items] * c]))
        return len(collections.Counter(arr[k:]))
