class Solution:
    # 8:23
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i =  0
        while(i < len(nums) and nums[i] == 0):
            i += 1
        
        first = i
        for j in range(i+1, len(nums)):
            if nums[j] == 0:
                continue
            else:
                second = j
                print((first, second))
                dis = second - first - 1
                if dis < k:
                    return False
                first  = second
        return True

