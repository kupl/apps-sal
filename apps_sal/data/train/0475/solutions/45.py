class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i,x in enumerate(nums):
            sums.append(x)
            for j,y in enumerate(nums[i+1:]):
                sums.append(sum(nums[i:i+j+2]))
        sums.sort()
        #print(sums)
        return sum(sums[left-1:right]) % (10**9 + 7)
