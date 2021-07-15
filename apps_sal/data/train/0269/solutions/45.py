class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        def find(nums, *argc):
            try:
                return nums.index(*argc)
            except ValueError:
                return -1
            
        prev = find(nums, 1)
        while prev != -1:
            cur = find(nums, 1, prev + 1)
            if cur != -1 and (cur - prev - 1) < k:
                return False
            prev = cur
        return True
