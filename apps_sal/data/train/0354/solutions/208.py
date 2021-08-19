class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        def helper(n, last, count):
            key = (n, last, count)
            if key in d:
                return d[key]
            if n == 0:
                return 1
            ans = 0
            for i in range(6):
                if i == last and count == rollMax[i]:
                    continue
                if i == last:
                    ans += helper(n - 1, i, count + 1)
                else:
                    ans += helper(n - 1, i, 1)
            d[key] = ans
            return d[key]
        d = dict()
        return helper(n, -1, 0) % (10 ** 9 + 7)
