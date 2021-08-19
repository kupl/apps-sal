class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        nums = sorted(nums)
        cnt = collections.Counter(nums)
        for x in nums:
            if cnt[x] == 0:
                continue
            for i in range(1, k):
                if cnt[x + i] > 0:
                    cnt[x + i] -= 1
                else:
                    return False
            cnt[x] -= 1
        return True
