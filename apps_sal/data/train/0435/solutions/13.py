class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sums = 0
        count = 0
        dic = {0:1}
        
        for a in A:
            sums = (sums + a) % K
            print(sums)
            if sums in dic:
                count += dic[sums]
                dic[sums] += 1
            else:
                dic[sums] = 1
                
        return count
