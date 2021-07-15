class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        sums = 0
        d = {0:1}
        for num in A:
            sums = (sums + num) % K
            # if sums < 0:
            #     sums += K
            res += d.get(sums, 0)
            d[sums] = d.get(sums, 0) + 1
        return res
    
    # [4,9,9,7,4,5]
    # d = {
    #     0:1, 4:4, 2:1, 
    # }
    # res = 7
    # sums = 4
        

