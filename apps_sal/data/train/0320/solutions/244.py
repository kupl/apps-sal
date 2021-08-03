class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        max_count = 0

        for num in nums:
            cnt = 0
            while num > 0:
                if num % 2 != 0:
                    num -= 1
                    ans += 1
                else:
                    num /= 2
                    cnt += 1
            max_count = max(max_count, cnt)

        return ans + max_count
