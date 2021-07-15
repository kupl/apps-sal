class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        memo = {0: 1}
        count = 0
        res = 0
        for n in nums:
            if n % 2 == 1:
                count += 1
            if count - k in memo:
                res += memo[count - k]
            memo[count] = memo.get(count, 0) + 1
        return res
