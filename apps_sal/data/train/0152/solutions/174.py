class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def check_works(position, m, dist):
            balls_to_place = m - 1
            last_ball_pos = 0
            for ind in range(last_ball_pos, len(position)):
                if position[ind] - position[last_ball_pos] >= dist:
                    balls_to_place -= 1
                    last_ball_pos = ind
                if balls_to_place == 0:
                    break
            if balls_to_place == 0:
                return 1
            else:
                return 0
        position.sort()
        lb = 1
        rb = 1000000000
        while lb != rb - 1:
            ret = check_works(position, m, int((lb + rb) / 2))
            if ret == 0:
                rb = int((lb + rb) / 2)
            else:
                lb = int((lb + rb) / 2)
            print(lb, rb)
        return lb
