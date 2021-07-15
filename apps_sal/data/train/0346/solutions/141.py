class Solution:
   def numberOfSubarrays(self, nums: List[int], k: int) -> int:            
    cnt = 0 
    items = [-1]
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            items.append(i)
    items.append(len(nums))

    for i in range(1, len(items) - k ):
        left = items[i] - items[i - 1]
        right = items[i + k] - items[i + k-1]
        cnt += left * right
    return cnt 


