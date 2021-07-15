class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_odd = defaultdict(int)
        prefix_odd[0] = 1
        ans = count = 0
        for num in nums:
            if num % 2:
                count += 1
            prefix_odd[count] += 1
        for p in prefix_odd:
            if p - k in prefix_odd:
                ans += prefix_odd[p] * prefix_odd[p - k]
        return ans
