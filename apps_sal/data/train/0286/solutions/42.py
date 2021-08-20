from math import factorial


class Solution:

    def getProbability(self, balls: List[int]) -> float:
        n = len(balls)
        a = [0] * n
        b = balls[:]

        def perm(xs):
            result = factorial(sum(xs))
            for x in xs:
                result = result / factorial(x)
            return result
        t = sum(balls) // 2

        def dfs(a, b, i, sa, sb):
            if sa > t:
                return 0
            if i == n:
                if sa != sb:
                    return 0
                ca = sum([1 for x in a if x > 0])
                cb = sum([1 for y in b if y > 0])
                return perm(a) * perm(b) if ca == cb else 0
            result = 0
            for j in range(b[i] + 1):
                a[i] += j
                b[i] -= j
                result += dfs(a, b, i + 1, sa + j, sb - j)
                a[i] -= j
                b[i] += j
            return result
        splits = dfs(a, b, 0, 0, sum(b))
        return round(splits / perm(balls), 5)
