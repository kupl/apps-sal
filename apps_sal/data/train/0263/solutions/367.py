class Solution:

    def knightDialer(self, n: int) -> int:
        nbrs = {1: [6, 8], 2: [9, 7], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        self.memo = {}

        def find_count(idx, num):
            if idx == n:
                return 1
            if (num, idx) in self.memo:
                return self.memo[num, idx]
            count = 0
            for nbr in nbrs[num]:
                count += find_count(idx + 1, nbr)
            self.memo[num, idx] = count
            return count
        ans = 0
        for i in range(10):
            ans += find_count(1, i)
        mod = 10 ** 9 + 7
        return ans % mod
