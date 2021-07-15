class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        
        for i in range(n):
            arr.append(nums[i])
            for j in range(i + 1, n):
                arr.append(arr[-1] + nums[j])
        
        arr.sort()
        
        return sum(arr[left - 1:right]) % (1000000007)
