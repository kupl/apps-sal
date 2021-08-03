class Solution:
    def knightDialer(self, n: int) -> int:
        next_move = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        memo = defaultdict(int)
        for i in range(10):
            memo[i] = 1

        for _ in range(n - 1):
            next_memo = defaultdict(int)
            for i in range(10):
                for next_step in next_move[i]:
                    next_memo[next_step] += memo[i]
                    next_memo[next_step] %= 10**9 + 7
            memo = next_memo
        return sum(memo.values()) % (10**9 + 7)
