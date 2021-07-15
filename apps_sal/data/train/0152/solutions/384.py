class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        
        position.sort()
        maxForce = (position[-1] - position[0]) // (m - 1)
        minForce = 1        
        
        while maxForce > minForce:
            maxMinForce = (maxForce + minForce + 1) // 2
            #print(minForce, maxForce, maxMinForce)
            if self.canPut(position, m, maxMinForce):
                minForce = maxMinForce
            else:
                maxForce = maxMinForce - 1
        
        return minForce
    
    def canPut(self, position: List[int], m: int, force: int) -> bool:
        putCnt = 0
        prePos = -1
        for pos in position:
            if prePos == -1 or pos - prePos >= force:
                putCnt += 1
                prePos = pos
                if putCnt == m:
                    return True
        
        return False
