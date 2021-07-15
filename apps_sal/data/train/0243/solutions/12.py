class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        minimum = 10000
        sames = []
        for front, back in zip(fronts,backs):
            
            if front == back:
                sames.append(front)
                
                
        for front,back in zip(fronts,backs):
            if front not in sames:
                minimum = min(front, minimum)
                
            if back not in sames:
                minimum = min(back, minimum)
                
        
        if minimum == 10000:
            return 0
        else:
            return minimum
