class Solution:
    adjacency = {0: {4, 6}, 1: {8, 6}, 2: {7, 9}, 3: {8, 4}, 4: {3, 9, 0}, 5: {}, 6: {1, 7, 0}, 7: {2, 6}, 8: {1, 3}, 9: {2, 4}}

    def knightDialer(self, n: int):
        count = [1 for _ in range(10)]
        for _ in range(n - 1):
            count = [sum((count[next_digit] for next_digit in Solution.adjacency[digit])) for digit in range(10)]
        return sum(count) % (10 ** 9 + 7)
