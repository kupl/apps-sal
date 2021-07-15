class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr) 
        return len(set(sorted(arr, key= lambda x: (c[x], x))[k:]))
                

