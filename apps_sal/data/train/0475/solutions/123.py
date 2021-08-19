class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l = 1
        ans = {0: [x for x in nums]}
        sums = [x for x in nums]
        while l <= len(nums) - 1:
            nxt = []
            prev = ans[l - 1]
            for i in range(len(prev)):
                if i + l >= len(nums):
                    break
                nxt.append(prev[i] + nums[i + l])
            ans[l] = nxt
            sums += nxt
            l += 1
        # print(sums)
        return sum(sorted(sums)[left - 1: right]) % 1000000007
