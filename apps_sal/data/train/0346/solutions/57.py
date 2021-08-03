class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        left = collections.defaultdict(int)
        odd = 0
        res = 0
        for n in nums:
            left[odd] += 1
            odd += n & 1
            if odd - k in left:
                res += left[odd - k]
        return res
