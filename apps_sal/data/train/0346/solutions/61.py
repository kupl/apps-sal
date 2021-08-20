class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        d[0] = 1
        cur_sum = 0
        ans = 0
        for (i, v) in enumerate(nums):
            cur_sum += v % 2
            if cur_sum - k in d:
                ans += d[cur_sum - k]
            d[cur_sum] += 1
        return ans
