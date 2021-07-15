def isOdd(num):
    return num % 2 == 1

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        items = [-1]
        for i, num in enumerate(nums):
            if isOdd(num):
                items.append(i)
        cnt = 0
        items.append(len(nums))
        for i in range(1, len(items) - 1):
            if i + k - 1 < len(items) - 1:
                left = items[i] - items[i-1]
                right = items[i+k] - items[i + k - 1]
                cnt += left * right
                    
        return cnt
