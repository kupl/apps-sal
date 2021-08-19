class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        h = []
        for i in range(len(nums)):
            s = 0
            for n in nums[i:]:
                s += n
                heappush(h, s)
        for _ in range(left - 1):
            heappop(h)
        ans = 0
        for _ in range(right - left + 1):
            ans += heappop(h)
        return ans % 1000000007
