class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        pos = sorted(position)
        l = 0
        r = pos[-1] - pos[0]
        while l < r:
            mid = (l + r + 1) // 2

            cum = pos[0]
            putted = 1
            for p in pos:
                if p >= cum + mid:
                    cum = p
                    putted += 1
            if putted >= m:
                l = mid
            else:
                r = mid - 1
        return l
