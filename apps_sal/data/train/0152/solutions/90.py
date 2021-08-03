class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def canFindGaps(d):
            left = 0
            found = i = 1
            while i < len(position) and found < m:
                if position[i] - position[left] >= d:
                    found += 1
                    left = i
                i += 1
            return found == m

        position.sort()
        max_diff = position[-1] - position[0]
        if m == 2:
            return max_diff

        left, right = 1, max_diff // (m - 1)
        while left < right:
            mid = (left + right) // 2
            if canFindGaps(mid):
                left = mid + 1
            else:
                right = mid - 1

        if right < left:
            return right
        return left if canFindGaps(left) else left - 1
