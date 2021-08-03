class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # if d*f < target:
        #     return 0
        # elif d*f==target:
        #     return 1

        faces = [i for i in range(1, f + 1)]
        cache = {}

        def dfs(left, numDice):
            re = 0
            if (left, numDice) in cache:
                return cache[(left, numDice)]
            if left > f * (d - numDice):
                # if left>f*d:
                cache[(left, numDice)] = 0
                return 0
            if numDice == d:
                # if d*f==
                return 1 if left == 0 else 0
            else:
                for face in faces:
                    numDice += 1
                    if left - face >= 0:
                        re += dfs(left - face, numDice)
                    numDice -= 1

                cache[(left, numDice)] = re
                return re
        return dfs(target, 0) % (10**9 + 7)
