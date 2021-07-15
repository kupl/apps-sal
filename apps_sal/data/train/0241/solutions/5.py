class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        move = {'N':(0,1), 'S':(0,-1), 'E':(1,0), 'W':(-1,0)}
        right = {'N':'E', 'S':'W', 'E':'S', 'W':'N'}
        left = {'N':'W', 'S':'E', 'E':'N', 'W':'S'}
        
        pos = (0,0)
        dire = 'N'
        i=0
        while i<4:
            for c in instructions:
                if c=='G':
                    x, y = pos
                    dx, dy = move[dire]
                    pos = (x+dx, y+dy)
                elif c=='L':
                    dire = left[dire]
                else:
                    dire = right[dire]
            
            if pos==(0,0) and dire=='N':
                return True
        
            i+=1
        
        return False
