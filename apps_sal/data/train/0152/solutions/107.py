class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 1, position[-1] - position[0]
        while l < r:
            mid = (l + r) // 2
            if self.check(position, mid, m):
                l = mid + 1
            else:
                r = mid
        return l if self.check(position, l, m) else l-1
    
    def check(self, position, k, m):
        last_placed_position = None
        for i,p in enumerate(position):
            if i == 0 or p-last_placed_position >= k:
                m -= 1
                if m == 0:
                    return True
                last_placed_position = p
        return False

