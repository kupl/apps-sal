class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = collections.Counter(arr)
        arr.sort()
        arr1 = sorted(arr, key=lambda x: counts[x])
        print(arr1)
        if k != 0:
            del arr1[:k]
            
        return len(set(arr1))
