class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)

        cache = dict()

        def solve(s):
            if s >= n:
                return 0

            if s in cache:
                return cache[s]

            best = -2**31
            presum = 0

            for x in range(1, 4):
                if s + x - 1 >= n:
                    break
                presum += stoneValue[s + x - 1]
                best = max(best, presum - solve(s + x))
            cache[s] = best
            return best
        score = solve(0)
        return 'Alice' if score > 0 else 'Bob' if score < 0 else 'Tie'
