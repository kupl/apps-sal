class Solution:
    def _MaxPossibleForce(self, position):
        return position[-1] - position[0]

    def _AssignBallsWithKDistance(self, position, force):
        i = 1
        assigned = 1
        # 0th item is the first ball
        last_assigned_position = 0
        while i < len(position):
            if position[i] - position[last_assigned_position] >= force:
                assigned += 1
                last_assigned_position = i
            i += 1
        return assigned

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        max_force = self._MaxPossibleForce(position)
        min_force = 1
        print((self._AssignBallsWithKDistance(position, 4)))
        while min_force <= max_force:
            search_force = (min_force + max_force) // 2
            num_assigned = self._AssignBallsWithKDistance(position, search_force)
            if num_assigned < m:
                max_force = search_force - 1
            else:
                min_force = search_force + 1
        return max_force
