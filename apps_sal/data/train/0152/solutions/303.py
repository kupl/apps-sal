class Solution:
    def checkDistance(self, position, minDist, m):
        lastBallPos = position[0]
        ballLeft = m - 1
        i = 1
        while i < len(position) and ballLeft != 0:
            if minDist <= position[i] - lastBallPos:
                lastBallPos = position[i]
                ballLeft -= 1
            i += 1
        return ballLeft == 0
    
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        high = 1000000000
        low = 1
        ans = 1
        while low < high:
            middle = (high + low + 1) // 2
            if self.checkDistance(position, middle, m):
                low = middle
            else:
                high = middle - 1
        return low
