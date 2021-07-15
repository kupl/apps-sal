class Solution:
    # https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431077/JavaC%2B%2BPython-One-Pass-O(1)-space
    def maxSumDivThree(self, nums: List[int]) -> int:
        seen = [0, 0, 0]
        for n in nums:
            # we need create a copy of seen, since we change element of seen in for loop.
            for j in [i + n for i in seen]:
                seen[j % 3] = max(seen[j % 3], j)
            # print('n = {0}, seen = {1}'.format(n, seen))
        return seen[0]
