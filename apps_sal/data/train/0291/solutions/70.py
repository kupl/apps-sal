class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        o = 0 
        e = 0 
        c = 0 
        p = 0

        for i in arr:
            p += i
            if p % 2 ==0:
                c += o
                e += 1
            else:
                c += e
                c += 1
                o += 1
        return c % 1000000007
