class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        l = {}
        for i in arr:
            if i in l:
                l[i] += 1
            else:
                l[i] = 1
        l = sorted(l.items(), key=lambda x: x[1])
        i = 0
        while k > 0:
            if l[i][1] <= k:
                k -= l[i][1]
            else:
                break
            i += 1
        return len(l) - i
