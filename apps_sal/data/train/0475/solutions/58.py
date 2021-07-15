class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        #two pointer approach? 
        sums = []
        for L in range(len(nums)):
            R = len(nums)
            #print(L,R)
            while(L<R):
                sums.append(sum(nums[L:R]))
                R-=1
        sums.sort()
        #print(sums)
        return sum(sums[left-1:right])%(10**9+7)
