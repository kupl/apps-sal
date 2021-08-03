class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        self.memo = {}
        self.result = 0
        for i in range(len(arr)):
            self.dfs(arr, i, d)
        return self.result

    def dfs(self, arr, index, d):
        if index in self.memo:
            return self.memo[index]
        result = 0
        for dir in [-1, 1]:
            for i in range(1, d + 1):
                j = index + i * dir
                if 0 <= j < len(arr) and arr[index] > arr[j]:
                    result = max(result, self.dfs(arr, j, d))
                else:
                    break
        self.memo[index] = result + 1
        self.result = max(self.result, result + 1)
        return result + 1
