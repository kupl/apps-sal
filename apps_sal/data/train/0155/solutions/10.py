class Solution:
    def helper(self, idx):
        if self.dp[idx] != float('inf'):
            return self.dp[idx]

        max_step = 1
        # to left
        for c in range(idx - 1, max(0, idx - self.d) - 1, -1):
            if self.arr[idx] <= self.arr[c]:
                break

            max_step = max(self.helper(c) + 1, max_step)

        # to right
        for c in range(idx + 1, min(self.n, idx + self.d + 1)):
            if self.arr[idx] <= self.arr[c]:
                break

            max_step = max(self.helper(c) + 1, max_step)

        self.dp[idx] = max_step
        return max_step

    def maxJumps(self, arr: List[int], d: int) -> int:
        self.n = len(arr)
        self.d = d
        self.arr = arr
        self.dp = [float('inf')] * self.n

        self.trans = defaultdict(list)

        max_ = 0
        for i in range(self.n):
            max_ = max(self.helper(i), max_)

        return max_
