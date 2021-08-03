class Solution:
    def getProbability(self, balls: List[int]) -> float:
        def factorial(k):
            if k <= 1:
                return 1
            return factorial(k - 1) * k

        def calc(balls):
            bs = [b for b in balls if b > 0]
            ans = factorial(sum(bs))
            for b in bs:
                ans /= factorial(b)
            return ans

        sols = []
        n = sum(balls) // 2

        def generate(sol, s, i):
            nonlocal sols
            if s > n:
                return

            if i == len(balls):
                if s == n:
                    sols += [sol]
                return

            for j in range(0, balls[i] + 1):
                generate(sol + [j], s + j, i + 1)
        generate([], 0, 0)

        count = 0
        memo = {}
        for sol in sols:
            l1 = sol
            l2 = [y - x for x, y in zip(l1, balls)]
            l1 = sorted([num for num in l1 if num > 0])
            l2 = sorted([num for num in l2 if num > 0])
            if len(l1) == len(l2):
                l = tuple(l1 + l2)
                if l not in memo:
                    memo[l] = calc(l1) * calc(l2)
                count += calc(l1) * calc(l2)

        return count / calc(balls)
