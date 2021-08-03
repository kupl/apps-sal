class Solution:
    def PredictTheWinner(self, nums):
        cache = {}

        def whose_turn(i, j):
            return (len(nums) - (j - i + 1)) % 2 == 0

        def traverse(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            p1_turn = whose_turn(i, j)

            if i == j:
                return (nums[i], 0) if p1_turn else (0, nums[i])

            if i + 1 == j:
                winning_move = max(nums[i], nums[j])
                losing_move = min(nums[i], nums[j])
                cache[(i, j)] = (winning_move, losing_move) if p1_turn else (losing_move, winning_move)
                return cache[(i, j)]

            p1_left, p2_left = traverse(i + 1, j)
            p1_right, p2_right = traverse(i, j - 1)

            if p1_turn:
                p1_move = max(p1_left + nums[i], p1_right + nums[j])
                p2_move = p2_left if p1_left + nums[i] >= p1_right + nums[j] else p2_right
            else:
                p1_move = p1_left if p2_left + nums[i] >= p2_right + nums[j] else p1_right
                p2_move = max(p2_left + nums[i], p2_right + nums[j])

            cache[(i, j)] = (p1_move, p2_move)
            return cache[(i, j)]

        p1_final, p2_final = traverse(0, len(nums) - 1)
        return p1_final >= p2_final
