class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        N = len(nums)
        
        prefix_sum = [0 for _ in range(N)]
        prefix_sum[0] = nums[0]
        for i in range(1, N):
            prefix_sum[i] = nums[i] + prefix_sum[i-1]
        
        # TODO: there is a bug here..not sure what the hell it is though!!!!
        prev_prefix = {}
        last_index = -1
        subarrays = 0
        for i in range(N):
            prefix = prefix_sum[i]
            
            to_look = prefix - target
            if to_look in prev_prefix and prev_prefix[to_look] >= last_index:
                last_index = i
                subarrays += 1
            elif nums[i] == target:
                subarrays += 1
                last_index = i
            elif prefix == target and last_index == -1:
                subarrays += 1
                last_index = i
                
            prev_prefix[prefix] = i
                
            
        return subarrays

