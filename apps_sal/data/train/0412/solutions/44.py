class Solution:
    def numRolls(self, d, f, target, memo):
        if target < d:
            return 0
        if d == 1:
            return int(target <= f)

        if (d, f, target) in memo:
            return memo[(d, f, target)]

        total = 0
        for new_target in range(target - f, target):
            total += self.numRolls(d - 1, f, new_target, memo)
            total = total % (10**9 + 7)
        memo[(d, f, target)] = total
        return total

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        ans = self.numRolls(d, f, target, memo)
        return ans
