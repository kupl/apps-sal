class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = (position[-1]-position[0]) // (m-1) + 1
        while left<right:
            mid = (left+right)//2
            if self.can(position, mid, m):
                left = mid + 1
            else:
                right = mid
        return left if self.can(position, left, m) else left-1
    
    def can(self, position, mid, m):
        n = len(position)
        pos = [0 for i in range(m)]
        i = 1
        j = 1
        while i < n and j < m:
            if position[i] - position[pos[j-1]] >= mid:
                pos[j] = i
                j += 1
            i += 1
        if j==m:
            return True
        return False
