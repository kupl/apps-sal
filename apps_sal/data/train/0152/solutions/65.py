class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        diff = position[-1] - position[0]
        right = diff // (m - 1)
        left = 1

        def condition(num):
            k = m - 1
            prev = position[0]
            for n in position[1:]:
                if n - prev >= num:
                    k -= 1
                    prev = n
                if k == 0:
                    return True
            return False

        while left < right:
            mid = left + (right - left) // 2
            # print(mid, condition(mid))
            if condition(mid):
                left = mid + 1
            else:
                right = mid
        if condition(left):
            return left
        else:
            return left - 1
        # print(left)
        return left
