class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        n = len(stoneValue)
        def solve(s):
            if s >= n: return 0
            elif s in memo :  return memo[s]
            currValue = 0
            best = -2**31
            for i in range(3):
                if s+i >= n:
                    break
                currValue += stoneValue[s+i]
                best = max(best, currValue - solve(s+i+1))
            memo[s] = best
            return best
        ans = solve(0)
        if ans > 0: return 'Alice'
        elif ans < 0 : return 'Bob'
        else: return 'Tie'
