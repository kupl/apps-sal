class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def backtrack(index=d - 1, target=target, dp={}):
            if index == -1 and target == 0:
                return 0
            if index < 0 or target <= 0:
                return None
            if (index, target) in dp:
                return dp[(index, target)]
            if target > f:
                start = f
            else:
                start = target
            count = 0
            for i in range(start, 0, -1):
                res = backtrack(index - 1, target - i, dp)
                if res != None:
                    count += res if res else 1
            dp[(index, target)] = count if count else None
            return dp[(index, target)]
        count = backtrack()
        return (count % (10**9 + 7)) if count != None else 0
