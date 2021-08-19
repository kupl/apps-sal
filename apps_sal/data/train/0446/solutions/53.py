class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if len(arr) == 0:
            return 0
        #sa = list(set(arr))
        arrcounts = collections.Counter(arr)  # [(x, arr.count(x)) for x in sa]
        # print(arrcounts)
        #arrcounts.sort(key = lambda x:x[1])
        arrcounts = sorted(arrcounts.items(), key=lambda x: x[1])
        i = k
        j = 0
        # print(arrcounts)
        while i > 0 and j < len(arrcounts):
            i -= arrcounts[j][1]
            if i >= 0:
                arrcounts.pop(j)
            else:
                j += 1
        # print(arrcounts)
        return len(arrcounts)
