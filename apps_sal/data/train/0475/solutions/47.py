class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ssum = nums[:]
        for ssize in range(2,n+1):
            ssum.extend([sum(nums[i:i+ssize]) for i in range(n-ssize+1)])
        ssum.sort()
        for i in range(n*(n+1)//2):
            ssum[i] %= int(1e9+7)
        return sum(ssum[left-1:right]) % int(1e9+7)
