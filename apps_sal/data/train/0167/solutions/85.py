class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        def f(x):
            ans = 0
            r = 1
            for i in range(1, K + 1):
                r *= (x - i + 1) / i
                #r //= i
                ans += r
                if ans >= N:
                    break
            return ans

        low, high = 1, N
        while low < high:
            middle = (low + high) // 2
            if f(middle) < N:
                low = middle + 1
            else:
                high = middle
        return low
