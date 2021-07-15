class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        countMap = Counter(nums)
        nums.sort()
        for num in nums:
            if countMap[num] == 0:
                continue
            for i in range(num, num+k):
                if countMap[i] > 0:
                    countMap[i] -= 1
                else:
                    return False
        return True
                

