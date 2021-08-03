class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = [nums[0]]
        for i in range(1, n):
            sums.append(sums[i - 1] + nums[i])
        for s in range(1, n):
            for e in range(s, n):
                sums.append(sums[e] - sums[s - 1])
        sums.sort()
        acc = 0
        for s in sums[left - 1:right]:
            acc = (acc + s) % (10**9 + 7)
        return acc
