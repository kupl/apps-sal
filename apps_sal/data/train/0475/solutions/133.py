class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    res = nums[i]
                else:
                    res = res + nums[j]

                sums.append(res)

        sums = sorted(sums)
        ans = sum(sums[k] for k in range(left - 1, right))
        return int(ans % (1e9 + 7))
