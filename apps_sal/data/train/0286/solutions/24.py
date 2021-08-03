class Solution:
    def getProbability(self, balls: List[int]) -> float:

        total = sum(balls)
        k = len(balls)

        def theSame(added):
            res = 0
            for i in range(k):
                if added[i] == 0:
                    res -= 1
                elif balls[i] == added[i]:
                    res += 1
            return res == 0

        def combination(this, pick):
            pick = min(this - pick, pick)
            res = 1
            i = this
            j = 1
            while i > pick:
                res *= i
                res /= j
                i -= 1
                j += 1
            return res

        def helper(i, added, cur):

            if cur == total // 2:

                if theSame(added):
                    res = 1
                    for i in range(k):
                        res *= combination(balls[i], added[i])
                    return res
                return 0
            if i == k:
                return 0
            if cur > total // 2:
                return 0
            res = 0
            for t in range(balls[i] + 1):
                added[i] = t
                res += helper(i + 1, added, cur + t)
            added[i] = 0
            return res

        added = [0] * k
        return helper(0, added, 0) / combination(total, total // 2)
