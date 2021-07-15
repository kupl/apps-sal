sys.setrecursionlimit(100000)
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @lru_cache(None)
        def f(n, last, consec):
            if n == 0: return 1
            if consec < rollMax[last]:
                A = f(n-1, last, consec+1)
            else:
                A = 0
            return (A + sum(f(n-1, i, 1) for i in range(6) if i != last)) % (10**9+7)
        return f(n, 0, 0)

