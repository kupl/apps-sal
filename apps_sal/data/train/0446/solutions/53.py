class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if len(arr) == 0:
            return 0
        arrcounts = collections.Counter(arr)
        arrcounts = sorted(arrcounts.items(), key=lambda x: x[1])
        i = k
        j = 0
        while i > 0 and j < len(arrcounts):
            i -= arrcounts[j][1]
            if i >= 0:
                arrcounts.pop(j)
            else:
                j += 1
        return len(arrcounts)
