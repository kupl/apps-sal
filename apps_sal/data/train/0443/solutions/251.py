class Solution:

    def numTeams(self, arr: List[int]) -> int:
        k = 3
        self.memo = {}
        ans = 0
        for i in range(len(arr)):
            ans += self.helper(i, arr, k - 1, True)
        self.memo = {}
        for i in range(len(arr)):
            ans += self.helper(i, arr, k - 1, False)
        return ans

    def helper(self, i, arr, k, lookForIncreasing):
        if k == 0:
            return 1
        if i == len(arr):
            return 0
        if (i, k) in self.memo:
            return self.memo[i, k]
        res = 0
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i] and lookForIncreasing:
                res += self.helper(j, arr, k - 1, lookForIncreasing)
            elif arr[j] < arr[i] and (not lookForIncreasing):
                res += self.helper(j, arr, k - 1, lookForIncreasing)
        self.memo[i, k] = res
        return res
