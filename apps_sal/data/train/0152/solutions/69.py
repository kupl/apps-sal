class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position = sorted(position)
        (low, high) = (1, position[-1])
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            prev = position[0]
            cnt = 1
            for pos in position[1:]:
                if pos - prev >= mid:
                    cnt += 1
                    prev = pos
            if cnt >= m:
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1
        return ans
