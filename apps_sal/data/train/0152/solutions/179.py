class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def check(target_min_force):
            put_count = 1
            cur_force = 0
            for i in range(1, n):
                cur_force += position[i] - position[i - 1]
                if cur_force >= target_min_force:
                    cur_force = 0
                    put_count += 1
                    if put_count == m:
                        return True
            return False
        (l, r) = (-1, position[-1] - position[0] + 1)
        while r - l > 1:
            mid = (l + r) // 2
            if check(mid):
                l = mid
            else:
                r = mid
        return l
