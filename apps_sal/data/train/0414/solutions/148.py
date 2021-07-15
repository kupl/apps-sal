class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        maxs = [arr[0]] * n
        for i in range(1, n):
            maxs[i] = max(maxs[i - 1], arr[i])
        for i in range(n):
            if maxs[i] == maxs[min(i + k, n - 1)]: return maxs[i]
            if i > 0 and maxs[i - 1] < maxs[i] == maxs[min(i + k - 1, n - 1)]: return maxs[i]
