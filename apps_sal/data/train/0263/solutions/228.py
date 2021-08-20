class Solution:

    def knightDialer(self, n: int) -> int:
        prior_case = [1] * 10
        current_case = [1] * 10
        paths = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        curr_hop = 1
        while curr_hop < n:
            curr_hop += 1
            current_case = [0] * 10
            for num in range(10):
                for neighbor in paths[num]:
                    current_case[num] += prior_case[neighbor]
            prior_case = current_case
        return sum(current_case) % (10 ** 9 + 7)
