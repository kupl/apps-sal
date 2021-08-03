class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        def helper(last, index, maxval):
            if index == n:
                return 1

            val = 0

            if (index, last, maxval) in dp:
                return dp[(index, last, maxval)]
            for i in range(6):
                if last == i:
                    if maxval + 1 > rollMax[i]:
                        continue
                    else:
                        val += helper(i, index + 1, maxval + 1)
                else:
                    val += helper(i, index + 1, 1)
            dp[(index, last, maxval)] = val % (10**9 + 7)
            return val

        dp = {}
        return helper(None, 0, 0) % (10**9 + 7)
