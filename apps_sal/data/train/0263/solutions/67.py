class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9],
                 [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        result = [1] * 10

        hops = 0
        while hops < n - 1:
            nextResult = [0] * 10
            for idx in range(len(result)):
                for step in moves[idx]:
                    nextResult[idx] += result[step]
            result = nextResult
            hops += 1

        return sum(result) % (10**9 + 7)
