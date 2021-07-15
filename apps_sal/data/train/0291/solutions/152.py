class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even, odd = 1, 0
        total = 0
        ans = 0
        for i in arr:
            total += i
            if total % 2 == 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
            ans %= 10**9 + 7
        return ans

