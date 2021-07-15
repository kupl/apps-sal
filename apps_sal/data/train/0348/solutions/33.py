class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        max_overall = arr[0]
        max_sum = arr[0]
        max_excluded = float('-inf')
        for i in range(1, len(arr)):
            max_excluded = max(max_excluded + arr[i], max_sum)
            max_sum = max(max_sum + arr[i], arr[i])
            max_overall = max(max_overall, max_sum, max_excluded)
        return max_overall

