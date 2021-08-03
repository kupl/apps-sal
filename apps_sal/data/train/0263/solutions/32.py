class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        cur_count = [1] * 10
        for _ in range(n - 1):
            next_count = [0] * 10
            for src_key in range(10):
                for dst_key in moves[src_key]:
                    next_count[dst_key] += cur_count[src_key]

            cur_count = next_count

        return sum(cur_count) % 1000000007
