class Solution:
    def is_force_valid(self, position: List[int], m: int, force: int) -> bool:
        last_pos = position[0]
        m -= 1
        for i in range(1, len(position)):
            if position[i] - last_pos >= force:
                m -= 1
                if m == 0:
                    return True
                last_pos = position[i]
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = position[-1] - position[0]

        while right > left:
            mid = (right + left + 1) // 2
            if self.is_force_valid(position, m, mid):
                left = mid
            else:
                right = mid - 1

        return left
