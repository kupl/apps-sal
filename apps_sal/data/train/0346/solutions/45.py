class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        (prefix, odd_cnt, ans) = ({0: 1}, 0, 0)
        for num in nums:
            if num % 2 == 1:
                odd_cnt += 1
            prefix[odd_cnt] = prefix.get(odd_cnt, 0) + 1
            if odd_cnt - k in prefix:
                ans += prefix[odd_cnt - k]
        return ans
