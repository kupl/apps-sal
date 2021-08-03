class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        # d stores elements seen till now against every cumsum
        d = {0: 0}
        start = {}
        cumsum = 0
        for i, num in enumerate(nums):
            cumsum += num % 2
            d[cumsum] = i + 1
            if (cumsum not in start):
                start[cumsum] = i
            if cumsum == k:
                elems = d[0]
                ans += elems + 1
            elif cumsum > k:
                elems = d[cumsum - k] - start.get(cumsum - k, -1)
                ans += elems
        return ans
