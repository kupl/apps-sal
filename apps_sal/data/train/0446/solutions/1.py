class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        unique = len(count)
        for v in sorted(count.values()):
            if v <= k:
                unique -= 1
                k -= v
            else:
                break
        return unique
