class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        pre = ans = 0
        for n in nums:
            pre += n & 1
            prefix[pre] += 1
            ans += prefix[pre - k]

        return ans
