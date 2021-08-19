class Solution:

    def max(self, arr, l, r):
        a = max(arr[l:r])
        self.mdp[l, r] = a
        return a

    def maxDp(self, arr, l, r):
        a = self.mdp.get((l, r), None)
        return self.max(arr, l, r) if a is None else a

    def mctFromSubArray(self, arr: List[int], l: int, r: int) -> int:
        if l == r - 1:
            return 0
        if l == r - 2:
            return arr[l] * arr[l + 1]
        return min((self.maxDp(arr, l, k) * self.maxDp(arr, k, r) + self.mctFromSubArrayDp(arr, l, k) + self.mctFromSubArrayDp(arr, k, r) for k in range(l + 1, r)))

    def mctFromSubArrayDp(self, arr: List[int], l: int, r: int) -> int:
        if (l, r) in self.dp:
            return self.dp[l, r]
        ans = self.mctFromSubArray(arr, l, r)
        self.dp[l, r] = ans
        return ans

    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.dp = {}
        self.mdp = {}
        return self.mctFromSubArrayDp(arr, 0, len(arr))
