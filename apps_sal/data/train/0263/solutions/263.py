class Solution:

    def knightDialer(self, n: int) -> int:
        G = {5: set(), 1: set([6, 8]), 3: set([4, 8]), 7: set([2, 6]), 9: set([2, 4]), 4: set([3, 9, 0]), 6: set([1, 7, 0]), 2: set([7, 9]), 8: set([1, 3]), 0: set([4, 6])}
        mem = dict()

        def dfs(val, rem):
            if (val, rem) in mem:
                return mem[val, rem]
            if rem == 1:
                return 1
            ans = 0
            for n in G[val]:
                ans += dfs(n, rem - 1)
            mem[val, rem] = ans
            return ans % (10 ** 9 + 7)
        ans = 0
        for i in range(10):
            ans += dfs(i, n)
        return ans % (10 ** 9 + 7)
