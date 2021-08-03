class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False

        count = Counter(nums)
        nums = sorted(count.keys())

        while nums:
            for num in range(nums[0], nums[0] + k):
                if num not in count or count[num] == 0:
                    return False
                count[num] -= 1
                if count[num] == 0:
                    nums.remove(num)

        return True
