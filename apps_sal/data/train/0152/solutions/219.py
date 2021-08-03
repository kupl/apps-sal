class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Binary search solution.
        # https://leetcode.com/problems/magnetic-force-between-two-balls/discuss/794070/Python-Binary-search-solution-with-explanation-and-similar-questions

        position.sort()

        def num_balls_placed(tested_distance):
            num_placed, current = 1, position[0]

            for i in range(1, len(position)):
                if position[i] - current >= tested_distance:
                    current = position[i]
                    num_placed += 1

            return num_placed

        low, high = 0, position[-1] - position[0]
        best = -1

        while low <= high:
            mid = (low + high) // 2

            if num_balls_placed(mid) < m:
                high = mid - 1
            else:
                best = mid
                low = mid + 1

        return best
