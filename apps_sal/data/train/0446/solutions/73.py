class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        count = sorted(count.values())
        a = len(count)
        for i in count:
            if k >= i:
                k -= i
                a -= 1
        return a
