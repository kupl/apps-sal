class Solution:
    def isValidStep(self, blocked, visited, step) -> bool:
        return tuple(step) not in blocked and tuple(step) not in visited and step[0] >= 0 and step[0] < 1000000 and step[1] >= 0 and step[1] < 1000000
    
    def isEscapePossibleHelper(self, blocked: set, source: List[int], target: List[int]) -> bool:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        nextSteps = []
        visited = set([tuple(source)])
        
        for d in directions:
            step = [source[0] + d[0], source[1] + d[1]]
            if self.isValidStep(blocked, visited, step):
                nextSteps.append(step)
                visited.add(tuple(step))

        while nextSteps:
            step = nextSteps.pop()
            if step == target or abs(step[0] - source[0]) + abs(step[1] - source[1]) >= 200:
                return True
            
            for d in directions:
                nextStep = [step[0] + d[0], step[1] + d[1]]
                if self.isValidStep(blocked, visited, nextStep):
                    nextSteps.append(nextStep)
                    visited.add(tuple(step))
                    if len(visited) > 20000:
                        return True

        return False
    
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(tuple(b) for b in blocked)
        return self.isEscapePossibleHelper(blocked, source, target) and self.isEscapePossibleHelper(blocked, target, source)
