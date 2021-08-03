class Solution:
    def find_right_max(self, arr):
        right_max = [arr[-1]]
        for i in range(len(arr) - 2, -1, -1):
            right_max.append(max(arr[i], right_max[-1]))

        return reversed(right_max)

    def maxWidthRamp(self, A: List[int]) -> int:
        indices_sort = [i[0] for i in sorted(enumerate(A), key=lambda x:x[1])]
        set_ele = set(A)
        indices = []
        for idx in indices_sort:
            if idx in set_ele:
                indices.append(idx)

        right_max = self.find_right_max(indices_sort)
        max_width_ramp = float('-inf')
        for idx, right_max in zip(indices_sort, right_max):
            max_width_ramp = max(right_max - idx, max_width_ramp)

        return max_width_ramp
