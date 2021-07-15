class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        a = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                a.add(fronts[i])
                
                
        l = []
        
        for i in range(len(fronts)):
            if fronts[i] not in a:
                # continue
                l.append(fronts[i])
            
            if backs[i] not in a: 
                l.append(backs[i])

        l.sort()
        
        if len(l) == 0:
            return 0
        
        return l[0]
