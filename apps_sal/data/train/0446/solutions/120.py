class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = collections.Counter(arr)
        arrs = sorted(arr, key=lambda x: (-dic[x], x))
    
        for i in range(k):
            arrs.pop()
        return len(set(arrs))
