class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        self.arr = arr
        self.dp = {}

        def helper(i, j, k):

            if j <= i:
                return 0

            if (i, j) in self.dp:
                return self.dp[(i, j)]

            maxsum = -sys.maxsize

            for length in range(1, k + 1):

                if i + length <= j:

                    currsum = (max(self.arr[i:i + length]) * length) + helper(i + length, j, k)
                    maxsum = max(maxsum, currsum)

            self.dp[(i, j)] = maxsum
            return self.dp[(i, j)]

        return helper(0, len(arr), k)
