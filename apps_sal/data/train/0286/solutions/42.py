from math import factorial

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        # number of distinct arrangements where some balls are identical
        # fact(sum(balls)) / fact(balls[0]) * fact(balls[1]) * .. * fact(balls[n - 1])

        n = len(balls)
        a = [0] * n
        b = balls[:]

        def perm(xs):
            # result = 1
            # j = 1
            # for i in range(n):
            #     for k in range(1, xs[i] + 1):
            #         result = result * j / k
            #         j += 1

            # return result

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



