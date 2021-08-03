class Solution:
    def knightDialer(self, n: int) -> int:
        possibilities = {2: {9, 7}, 1: {8, 6}, 3: {4, 8}, 4: {3, 9, 0}, 5: {}, 6: {1, 7, 0}, 7: {6, 2}, 8: {1, 3}, 9: {4, 2}, 0: {4, 6}}

        def dp(n):
            result = {i: 1 for i in range(10)}
            for i in range(2, n + 1):
                temp = defaultdict(int)
                for curr_position in result:
                    for next_position in possibilities[curr_position]:
                        temp[next_position] += result[curr_position]
                result = temp
            return sum(result.values()) % (pow(10, 9) + 7)

        return dp(n)
