class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        map = {}
        map[0] = 1
        sum, count = 0, 0
        
        for n in A:
            sum = (sum + n) % K
            
            if sum not in list(map.keys()):
                map[sum] = 1
            else:
                count += map[sum]
                map[sum] += 1
        
        return count

