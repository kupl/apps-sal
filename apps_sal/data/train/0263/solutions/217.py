from collections import deque

MOD = 10 ** 9 + 7


class Solution:
    def knightDialer(self, n: int) -> int:
        m = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        curt = {i: 1 for i in range(0, 10)}
        n -= 1

        while n > 0:
            next_set = {}
            for key in curt:
                for nei in m[key]:
                    next_set[nei] = (next_set.get(nei, 0) + curt[key]) % MOD

            curt = next_set
            n -= 1

        return sum(curt.values()) % MOD
