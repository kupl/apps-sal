class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(f):
            nonlocal position
            nonlocal m
            nonlocal res
            for i in range(len(position)):
                balls_cnt = 1
                last_ball_pos = 0

                for i in range(1, len(position)):
                    last_ball_val_pos = position[last_ball_pos]
                    curr_ball_val_pos = position[i]
                    cur_force = curr_ball_val_pos - last_ball_val_pos
                    if cur_force >= f:
                        balls_cnt += 1
                        last_ball_pos = i
                        if balls_cnt == m:
                            res = max(res, f)
                            return True

                return False

        res = 0
        position.sort()
        left = 1
        right = position[-1]

        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                # add to answer, check if can do better increase mid and look up in right part
                left = mid + 1
            else:
                right = mid

        return res
