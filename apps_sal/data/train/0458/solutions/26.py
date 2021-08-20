class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        min_l = float('inf')
        accu = 0
        c = sum(nums) % p
        dic = {}
        for (i, num) in enumerate(nums):
            accu += num
            ci = accu % p
            dic[ci] = i
            t = (ci - c) % p
            if t in dic:
                min_l = min(min_l, i - dic[t])
            if i != len(nums) - 1 and ci == c:
                min_l = min(min_l, i + 1)
        return min_l if min_l != float('inf') else -1
