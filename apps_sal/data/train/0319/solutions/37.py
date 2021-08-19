class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # Get the highest socre of Alice s1,
        # then score of Bob is sum(stoneValue) - s.
        # If s1 > s2 => Alice, if s1 == s2 => Tie, else
        # Bob

        # [1,2,3,6]
        # TLE, because in getScore we have to sum(stoneValue) since we
        # don't need to get the explict score, we can optimize it, which
        # is the second approach.
        #         memo = {}
        #         def getScore(start):
        #             if start >= len(stoneValue):
        #                 return 0
        #             if start in memo:
        #                 return memo[start]
        #             res = -math.inf
        #             front = 0
        #             behind = sum(stoneValue[start:])
        #             for i in range(start, min(start+3, len(stoneValue))):
        #                 front += stoneValue[i]
        #                 behind -= stoneValue[i]
        #                 cur = front + behind - getScore(i+1)
        #                 res = max(cur, res)

        #             return res

        #         s1 = getScore(0)
        #         s2 = sum(stoneValue) - s1

        #         if s1 > s2:
        #             return 'Alice'
        #         elif s1 == s2:
        #             return 'Tie'
        #         else:
        #             return 'Bob'

        # Second approach
        memo = {}

        def dfs(start):
            if start >= len(stoneValue):
                return 0
            if start in memo:
                return memo[start]
            memo[start] = -math.inf
            score = 0
            for i in range(start, min(len(stoneValue), start + 3)):
                score += stoneValue[i]
                memo[start] = max(memo[start], score - dfs(i + 1))

            return memo[start]
        score = dfs(0)

        if score > 0:
            return 'Alice'
        elif score == 0:
            return 'Tie'
        else:
            return 'Bob'
