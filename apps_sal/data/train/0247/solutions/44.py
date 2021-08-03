class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        def aux(arr):
            h = {0: 0}
            preSum = 0
            left = [n + 1 for i in range(n)]
            for i in range(1, n + 1):
                preSum = preSum + arr[i - 1]
                h[preSum] = i
                if preSum - target in h:
                    left[i - 1] = i - h[preSum - target]
                if i > 1:
                    left[i - 1] = min(left[i - 2], left[i - 1])
            return left

        left = aux(arr)
        arr.reverse()
        right = aux(arr)

        # print(left)
        # print(right)

        ans = n + 1
        for i in range(n - 1):
            ans = min(ans, left[i] + right[n - 1 - (i + 1)])
        return ans if ans < n + 1 else -1
