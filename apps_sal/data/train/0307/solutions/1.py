class Solution:
    mem = {}

    def soupServings(self, N: int) -> float:
        if N > 4800:
            return 1

        def empty(a, b):
            if (a, b) in self.mem:
                return self.mem[(a, b)]
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            ans = 0.25 * (empty(a - 4, b) + empty(a - 3, b - 1) + empty(a - 2, b - 2) + empty(a - 1, b - 3))
            self.mem[(a, b)] = ans
            return ans
        N = math.ceil(N / 25)
        return empty(N, N)
