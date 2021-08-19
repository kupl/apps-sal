class Solution:

    def knightDialer(self, n: int) -> int:

        def knight_dailer(n):
            paths = {0: [4, 6], 1: [6, 8], 2: [9, 7], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [6, 2], 8: [1, 3], 9: [4, 2]}
            count = 0
            import sys
            import functools
            sys.setrecursionlimit(10 ** 9)

            @functools.lru_cache(None)
            def traverse(i, rem):
                if rem == 0:
                    return 1
                ans = 0
                for p in paths[i]:
                    res = traverse(p, rem - 1)
                    ans += res
                return ans
            for i in range(10):
                count += traverse(i, n - 1)
            return count % (10 ** 9 + 7)
        return knight_dailer(n)
