class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnts = Counter(arr)
        
        sorted_cnts = sorted(cnts.items(), key=lambda x: x[1])
        for key, val in sorted_cnts:
            if val <= k:
                del cnts[key]
                k -= val
            else:
                break
        return len(cnts)
