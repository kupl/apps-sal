class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        values = [[v, k] for (k, v) in list(d.items())]
        values.sort()
        for i in values:
            if i[0] <= k:
                k = k - i[0]
                i[0] = 0
        count = 0
        for i in values:
            if i[0] != 0:
                count = count + 1
        return count
