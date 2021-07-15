class Solution:
    def knightDialer(self, n: int) -> int:
        next = {1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: (),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4),
            0: (4, 6),
           }
        M = 1000000007
        # cache = {}
        cache = defaultdict(int)
        def helper(m, n):
            if (m, n) not in cache:
                # cache[m,n] = []
                if n == 1:
                    cache[m,n] = 1
                else:
                    for nn in next[m]:
                        # for e in helper(nn, n-1):
                        #     cache[m,n].append([m] + e)
                        cache[m,n] += helper(nn, n-1)
                cache[m,n] %= M
            return cache[m,n] 

        # res = []
        # for i in range(10):
        #    res.extend(helper(i, n))
        # return res

        return sum(helper(i, n) for i in range(10)) % M
