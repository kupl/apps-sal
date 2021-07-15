class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l,r = left-1,right-1
        cur = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                cur.append(sum(nums[i:j+1]))
        cur.sort()
        return sum(cur[l:r+1]) %(10**9+7)
