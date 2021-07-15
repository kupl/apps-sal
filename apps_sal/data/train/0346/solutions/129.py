class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddIdx = []
        
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                oddIdx.append(i)
            
        if len(oddIdx) < k:
            return 0
        
        arr = [oddIdx[0] + 1]
        for i in range(1, len(oddIdx)):
            temp = oddIdx[i] - oddIdx[i - 1]
            arr.append(temp)
        arr.append(len(nums) - oddIdx[-1])
            
        res = 0
        for i in range(len(arr) - k):
            res += arr[i] * arr[i + k]
        
        return res
