class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)

        def is_good(position, target_distance, m):
            prev = position[0]
            count = 1
            for i in range(1, len(position)):
                pos = position[i]
                if pos - prev >= target_distance:
                    prev = pos
                    count += 1
                    if count == m:
                        return True
            return False
        left = 1
        right = max(position)
        while right > left + 1:
            mid = (left + right) // 2
            if is_good(position, mid, m):
                left = mid
            else:
                right = mid
        if is_good(position, right, m):
            return right
        else:
            return left
