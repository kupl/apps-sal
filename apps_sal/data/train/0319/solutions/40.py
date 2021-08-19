class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # 采用和类似于stoneGameII的方法，可以吗？
        # 残局
        # solve(s) score diff
        # M=1,2,3
        # x=[1,2,3]
        # solve(s) = max(sum(sv[s:s+x-1]) - solve(s+x))

        n = len(stoneValue)

        cache = dict()  # s:score

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
