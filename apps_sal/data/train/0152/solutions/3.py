class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        sorted_position = sorted(position)
        
        N = len(position)
        lo = 1
        hi = sorted_position[N-1] - sorted_position[0]
        
        last_achieved = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self._try_target(mid, sorted_position, m):
                lo = mid+1
                last_achieved = mid
            else:
                hi = mid-1
        
        return last_achieved
    
    def _try_target(self, target: int, positions: List[int], m:int) -> bool:
        slotted = 1
        last_slotted = positions[0]
        
        for i in range(1, len(positions)):
            if positions[i] - last_slotted >= target:
                slotted += 1
                last_slotted = positions[i]
        
        return slotted >= m

