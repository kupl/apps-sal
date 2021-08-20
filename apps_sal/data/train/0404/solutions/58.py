class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        memo = {}

        def fn(nums, k):
            if len(nums) <= k:
                return sum(nums)
            elif k == 1:
                return sum(nums) / len(nums)
            else:
                max_avg = 0
                for i in reversed(range(len(nums))):
                    key = (tuple([num for num in nums[:i]]), k - 1)
                    if key not in memo:
                        memo[key] = fn([num for num in nums[:i]], k - 1)
                    avg = memo[key] + sum(nums[i:]) / (len(nums) - i)
                    max_avg = max(max_avg, avg)
                return max_avg
        return fn(A, K)
