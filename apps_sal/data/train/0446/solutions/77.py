class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        
        for elem, cnt in sorted(counter.items(), key = lambda x: x[1]):
            k -= cnt
            if k >= 0:
                del counter[elem]
        return len(counter)
