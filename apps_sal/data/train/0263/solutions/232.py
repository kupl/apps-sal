class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {
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

        count = 0
        num_each_digit = {
            0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1
        }
        for i in range(1, n + 1):
            count = sum(num_each_digit.values())
            temp_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            for digit in num_each_digit:
                num_digit = num_each_digit[digit]
                digit_neighbors = neighbors[digit]
                for neighbor in digit_neighbors:
                    temp_dict[neighbor] += num_digit
            num_each_digit = temp_dict
        return count % (10**9 + 7)
