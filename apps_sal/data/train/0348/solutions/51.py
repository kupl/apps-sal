class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        N = len(arr)
        max_ending_here0 = [0] * N
        max_ending_here1 = [0] * N
        max_ending_here0[0] = arr[0]
        max_ending_here1[0] = arr[0]
        max_ending_here0[1] = max(max_ending_here0[0] + arr[1], arr[1])
        max_ending_here1[1] = max(max_ending_here1[0] + arr[1], arr[1])
        for i in range(2, N):
            max_ending_here0[i] = max(max_ending_here0[i - 1] + arr[i], arr[i])
            max_ending_here1[i] = max(max_ending_here1[i - 1] + arr[i], max_ending_here0[i - 2] + arr[i], arr[i])
        return max(max_ending_here1)
