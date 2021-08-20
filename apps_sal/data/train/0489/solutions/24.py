class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        val_pos_list = [(value, pos) for (pos, value) in enumerate(A)]
        val_pos_list.sort()
        rightmost = len(A) - 1
        visited_pos = set()
        result = 0
        for (value, pos) in val_pos_list:
            while rightmost in visited_pos:
                rightmost -= 1
            distance = max(0, rightmost - pos)
            result = max(result, distance)
            visited_pos.add(pos)
        return result
