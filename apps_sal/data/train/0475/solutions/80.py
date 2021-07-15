class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        presum = [0] + list(accumulate(nums))
        arr = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                arr.append(presum[j] - presum[i])
        arr.sort() 
        return sum(arr[left-1:right]) % (10**9 + 7)
