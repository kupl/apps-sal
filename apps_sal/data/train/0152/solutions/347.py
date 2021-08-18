class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1
        r = position[-1]
        pos = 0
        print((l, r))

        def check(mid):
            cow_cnt = 1
            last_pos = position[0]
            for i in range(1, len(position)):
                if position[i] - last_pos >= mid:
                    cow_cnt += 1
                    if cow_cnt == m:
                        return True
                    last_pos = position[i]
            return False

        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                pos = mid
                l = mid + 1
            else:
                r = mid - 1
        return pos
