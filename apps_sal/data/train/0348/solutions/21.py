class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        res = float('-inf')
        max_ending_here0 = 3 * [arr[0]]
        max_ending_here1 = 3 * [arr[0]]
        for i in range(1, len(arr)):
            max_ending_here0[i % 3] = max(max_ending_here0[(i - 1) % 3] + arr[i], arr[i])
            max_ending_here1[i % 3] = max(max_ending_here1[(i - 1) % 3] + arr[i], arr[i])
            if i >= 2:
                max_ending_here1[i % 3] = max(max_ending_here1[i % 3], max_ending_here0[(i - 2) % 3] + arr[i])
            res = max(res, max_ending_here1[i % 3])
        return res
