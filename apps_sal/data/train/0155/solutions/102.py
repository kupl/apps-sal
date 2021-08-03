class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        def helper(i):
            if cache[i]:
                return cache[i]
            # go right
            numberOfJump = 0
            for j in range(i + 1, i + d + 1):
                if j >= len(arr) or arr[j] >= arr[i]:
                    break
                numberOfJump = max(helper(j), numberOfJump)
            for j in range(i - 1, i - d - 1, -1):
                if j < 0 or arr[j] >= arr[i]:
                    break
                numberOfJump = max(helper(j), numberOfJump)

            cache[i] = 1 + numberOfJump
            return cache[i]

        cache = [0] * len(arr)
        ans = 0
        for i in range(len(arr)):
            ans = max(helper(i), ans)
        return ans
