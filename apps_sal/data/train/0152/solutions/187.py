class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        highest_f = int((position[-1] - position[0]) / (m - 1))

        def helper(position, m, high_f, low_f, curr_f):
            selected_pos = [position[0]]
            for i in position:
                if i - selected_pos[-1] >= curr_f:
                    selected_pos.append(i)
            if high_f > low_f + 1:
                if len(selected_pos) < m:
                    new_curr_f = int((low_f + curr_f) / 2)
                    return helper(position, m, curr_f, low_f, new_curr_f)
                else:
                    new_curr_f = int((curr_f + high_f) / 2)
                    return helper(position, m, high_f, curr_f, new_curr_f)
            elif len(selected_pos) < m:
                return low_f
            else:
                return curr_f
        return int(helper(position, m, highest_f, 1, highest_f))
