class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        max_distance_between = (position[-1] - 1) // (m - 1)
        min_distance_between = 1
        if self.isDistancePossible(max_distance_between, position, m):
            return max_distance_between
        while max_distance_between > min_distance_between + 1:
            middle_distance = (min_distance_between + max_distance_between) // 2
            if self.isDistancePossible(middle_distance, position, m):
                min_distance_between = middle_distance
            else:
                max_distance_between = middle_distance
        return min_distance_between

    def isDistancePossible(self, distance, position, m):
        used_ball_count = 0
        previous_used_position = float('-inf')
        for pos in position:
            if pos - previous_used_position >= distance:
                used_ball_count += 1
                previous_used_position = pos
        return used_ball_count >= m
