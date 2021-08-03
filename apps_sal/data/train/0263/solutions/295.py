class Solution:
    def knightDialer(self, n: int) -> int:
        mapping = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        memo = {}

        def helper(num, total):
            if (num, total) in memo:
                return memo[(num, total)]
            if total == 0:
                return 1
            count = 0
            for next_num in mapping[num]:
                count += helper(next_num, total - 1)
            memo[(num, total)] = count
            return count
        count = 0
        for i in range(10):
            count += helper(i, n - 1)
        return count % (10**9 + 7)
