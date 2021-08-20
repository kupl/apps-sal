class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def helper(dist):
            count = 1
            prev = position[0]
            for i in range(1, len(position)):
                if position[i] - prev >= dist:
                    prev = position[i]
                    count += 1
            return count
        low = 1
        high = position[-1] - position[0]
        res = float('-inf')
        while low <= high:
            mid = low + (high - low) // 2
            if helper(mid) < m:
                high = mid - 1
            else:
                res = max(res, mid)
                low = mid + 1
        return res
