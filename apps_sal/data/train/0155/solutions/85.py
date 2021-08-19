class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        maxPath = 0
        memory = {i: 0 for i in range(len(arr))}
        for i in range(len(arr)):
            maxPath = max(maxPath, self.dfs(i, d, arr, len(arr), memory))
        return maxPath

    def dfs(self, index, d, arr, arrLen, memory):
        if memory[index] != 0:
            return memory[index]
        currentMax = 0
        for i in range(index + 1, index + d + 1):
            if i >= arrLen or arr[index] <= arr[i]:
                break
            currentMax = max(currentMax, self.dfs(i, d, arr, arrLen, memory))
        for i in range(index - 1, index - d - 1, -1):
            if i < 0 or arr[index] <= arr[i]:
                break
            currentMax = max(currentMax, self.dfs(i, d, arr, arrLen, memory))
        memory[index] = currentMax + 1
        return memory[index]
