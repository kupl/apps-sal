import bisect


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position_set = set(position)
        position.sort()
        max_force = (position[-1] - position[0]) // (m - 1)
        min_force = 1
        last_idx = len(position) - 1

        while min_force != max_force:
            mid_force = (min_force + max_force + 1) // 2
            first_ball = next_ball = position[0]
            next_idx = 1

            for _ in range(m - 2):
                next_ball = first_ball + mid_force

                if next_ball not in position_set:

                    # search the next larger
                    next_idx = bisect.bisect_left(position, next_ball, next_idx, last_idx)
                    next_ball = position[next_idx]
                    if next_idx == last_idx:
                        break

                next_idx += 1
                first_ball = next_ball
            else:
                if position[-1] - next_ball >= mid_force:
                    min_force = mid_force
                else:
                    max_force = mid_force - 1
                continue
            max_force = mid_force - 1

        return min_force
