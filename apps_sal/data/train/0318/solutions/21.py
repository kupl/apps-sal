class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:

        def find(arr, n):
            dp1 = [0 for i in range(n + 1)]
            dp2 = [0 for i in range(n + 1)]
            dp2[1] = arr[0]
            for i in range(1, len(arr)):
                new_dp1 = [max(dp1[j], dp2[j]) for j in range(n + 1)]
                new_dp2 = [0] + [arr[i] + dp1[j - 1] for j in range(1, n + 1)]
                dp1 = new_dp1
                dp2 = new_dp2
            return max(dp2[-1], dp1[-1])
        n = len(slices) // 3
        return max(find(slices[:-1], n), find(slices[1:], n))
