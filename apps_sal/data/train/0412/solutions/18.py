class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        def helper(d, target):
            if d == 0:
                 return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[(d,target)]
            to_return = 0
            for k in range(max(0, target-f), target):
                to_return += helper(d-1, k)
            memo[(d, target)] = to_return
            return to_return
        return helper(d, target) % (10**9 + 7)

