class Solution:
    def getProbability(self, balls: List[int]) -> float:
        def calc(d):
            n = len(d)
            s = sum(d.values())
            result = math.factorial(s)
            for k, v in list(d.items()):
                result /= math.factorial(v)
            return result
        
        def choose(i, k, d1, d2):
            if k == 0 and i <= n:
                for j in range(i, n):
                    d2[j] = balls[j]
                t = calc(d1) * calc(d2)
                e = t if len(d1) == len(d2) else 0
                return t, e 
            if k < 0 or i == n:
                return 0, 0
            t, e = 0, 0
            for j in range(balls[i] + 1):
                if j > 0:
                    d1[i] = j
                if balls[i] - j > 0:
                    d2[i] = balls[i] - j
                else:
                    d2.pop(i)
                a, b = choose(i + 1, k - j, d1, d2)
                t += a
                e += b
            if i in d1:
                d1.pop(i)
            if i in d2:
                d2.pop(i)
            return t, e
        
        n = len(balls)
        k = sum(balls) // 2
        t, e = choose(0, k, {}, {})
        # print(t, e)
        return e / t
            

