class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > d * f or target < d:
            return 0
        targets = {}
        faces = [i for i in range(1, f + 1)]

        def solve(target, numDice):
            ways = 0
            if (target, numDice) in targets:
                return targets[target, numDice]
            if target > f * (d - numDice):
                targets[target, numDice] = 0
                return 0
            if numDice == d:
                return 1 if target == 0 else 0
            else:
                for face in faces:
                    if target - face >= 0:
                        ways += solve(target - face, numDice + 1)
                targets[target, numDice] = ways
                return ways
        return solve(target, 0) % (10 ** 9 + 7)
