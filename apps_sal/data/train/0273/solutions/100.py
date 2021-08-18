class Solution:
    def racecar(self, target: int) -> int:

        targetLen = len(bin(target)) - 2
        barrier = (1 << targetLen)
        stack = [(0, target)]
        dp = {target: 0}

        while stack:
            step0, dist = heapq.heappop(stack)

            for i in range(targetLen + 1):
                move = (1 << i) - 1
                step1 = step0 + i
                if move != dist:
                    step1 += 1
                newDist = -(dist - move)
                if abs(newDist) <= barrier and (newDist not in dp or dp[newDist] > step1):
                    heapq.heappush(stack, (step1, newDist))
                    dp[newDist] = step1

        return dp[0]
