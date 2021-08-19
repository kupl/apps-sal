class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        size = len(position)

        def satisfy(gap) -> bool:
            """
            input: gap
            output: True, if m balls can be placed with distance >= gap.
                    False, otherwise.
            """
            next_valid_pos = position[0] + gap
            good_positions = 1
            for idx in range(1, size):
                if position[idx] >= next_valid_pos:
                    good_positions += 1
                    next_valid_pos = position[idx] + gap
                if good_positions == m:
                    return True
            return False
        position.sort()
        max_gap = (position[-1] - position[0]) // (m - 1)
        min_gap = min((position[i] - position[i - 1] for i in range(1, size)))
        if m == 2:
            return max_gap
        (left, right) = (min_gap, max_gap)
        while left <= right:
            gap_trial = left + (right - left) // 2
            if satisfy(gap=gap_trial):
                left = gap_trial + 1
            else:
                right = gap_trial - 1
        return left - 1
