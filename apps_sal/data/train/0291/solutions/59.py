class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = odd = even = 0
        for x in arr:
            even += 1
            if x % 2 != 0:
                even,odd = odd,even
                
            res = (res + odd) % (10 ** 9 + 7)
        return res

