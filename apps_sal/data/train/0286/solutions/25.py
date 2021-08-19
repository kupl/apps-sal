class Solution:
    def getProbability(self, balls: List[int]) -> float:
        def calc(d):
            n = len(d)
            s = sum(d.values())
            result = math.factorial(s)
            for k, v in list(d.items()):
                result /= math.factorial(v)
            return result

        t, e = 0, 0

        def choose(i, k, d1, d2):
            nonlocal t
            nonlocal e
            if k == 0 and i <= n:
                for j in range(i, n):
                    d2[j] = balls[j]
                t_ = calc(d1) * calc(d2)
                t += t_
                e += t_ if len(d1) == len(d2) else 0
                return
            if k < 0 or i == n:
                return
            for j in range(balls[i] + 1):
                if k - j < 0:
                    break
                if j > 0:
                    d1[i] = j
                if balls[i] - j > 0:
                    d2[i] = balls[i] - j
                else:
                    d2.pop(i)
                choose(i + 1, k - j, d1, d2)
            if i in d1:
                d1.pop(i)
            if i in d2:
                d2.pop(i)

        n = len(balls)
        k = sum(balls) // 2
        choose(0, k, {}, {})
        # print(t, e)
        return e / t
