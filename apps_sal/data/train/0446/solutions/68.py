#from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0
        dic = collections.Counter(arr)
        L = sorted(list(dic.values()))

        while k >= L[0]:
            k -= L.pop(0)
            if len(L) == 0:
                return 0
        return len(L)
