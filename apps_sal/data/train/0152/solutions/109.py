class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        def small_enough(mid):
            count = prev = 0
            for i, p in enumerate(position):
                if i == 0:
                    count += 1
                elif p - prev >= mid:
                    count += 1
                else:
                    continue
                prev = p
            return count >= m
        
        l, h = 1, position[-1] - position[0]
        while l < h:
            mid = (l + h + 1) // 2
            if small_enough(mid):
                l = mid
            else:
                h = mid - 1
        return l
