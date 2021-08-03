class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        mem = [0] * len(arr)

        def dfs(i):
            if mem[i]:
                return mem[i]
            num = 1

            j = i + 1
            while j in range(i + 1, min(len(arr), i + d + 1)) and arr[j] < arr[i]:
                num = max(num, dfs(j) + 1)
                j += 1

            j = i - 1
            while j in range(max(0, i - d), i) and arr[j] < arr[i]:
                num = max(num, dfs(j) + 1)
                j -= 1

            mem[i] = num
            return mem[i]

        res = 0
        for i in range(len(arr)):
            dfs(i)
            res = max(res, dfs(i) + 1)

        return max(mem)
