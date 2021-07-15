class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        sarray = []
        mod = 10**9+7
        for i in range(n):
            for j in range(i, n):
                sarray.append(sum(nums[i:j+1]))
        sarray.sort()
        
        return sum(sarray[left-1:right]) % mod
                

