class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = collections.Counter()
        cnt[0], odd, res = 1, 0, 0
        for i in nums:
            if i % 2 == 1:
                odd += 1
            cnt[odd] += 1
            res += cnt[odd - k]
        return res
